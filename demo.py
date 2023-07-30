"""
This file will be testing large language models from transformers being used in tandem with pdf_parser and html_parser to extract descriptions of chemical separations from research papers.
Author: Logan Endes https://github.com/Log45

Goals: Using few-shot CoT, answer these questions with different prompts
    - What is the target?
    - What is the target disolved in?
    - What is the resin (column) used?
    - What is the column eluted with?
    - What are the products?
    - (maybe) How long was the target irradiated?
    - (maybe) How long did the separation process take?
"""
import time
import torch
from html_parser import html_to_context
from pdf_parser import pdf_to_context
from transformers import AutoTokenizer, OPTForCausalLM, AutoModelForCausalLM, BloomForCausalLM, BloomTokenizerFast, GPTNeoXForCausalLM, LlamaTokenizer

keywords = {"separation", "Separation", "isolation", "Isolation", "chromatography", "Chromatography", "ion exchange", "ion Exchange", "Ion Exchange", "Ion exchange",
            "eluted", "Eluted", "elution", "Elution", "elute", "Elute", "fraction", "Fraction", "resin", "Resin", "exchange", "Exchange", "acid", "Acid", "target", "Target"}

example_context = "After irradiation of 5 h, the 64Ni target was dissolved in 6 M hydrochloride acid, and then the solution was load to an anion exchange column to separate into different components. The 64Ni was washed out with 6 M HCl and collected for recycling. Due to the elevated cost of enriched 64Ni, recycling of the target material for re-use could reduce the production cost of 64Cu, without sacriﬁcing the quality of subsequent 64Cu production. When the eluted was switched to 1 M HCl, the ﬁrst band coming out was co-produced cobalt radioisotopes (approximately 1 mL), and the second was the 64Cu, which was collected and evaporated to dryness. The residue was dissolved in 0.1 M HCl for further use. The separation process of 64Cu took about 2.5 h after irradiation."

target_question = "What is the target material in the above reaction?"
target_example_answer = "Since they say: 'the 64Ni target was dissolved in 6 M hydrochloride acid', then 64Ni, or Nickel-64, must be the target."

acid_question = "What acid is the target material dissolved in during the above reaction?"
acid_example_answer = "Since they say: 'the 64Ni target was dissolved in 6 M hydrochloride acid', then 6M hydrochloride acid must be the acid used to dissolve the target."

resin_question = "What resin/column is the solution loaded into during the above reaction?"
resin_example_answer = "Since they say: 'the solution was load to an anion exchange column to separate into different components', and an 'anion exchange column' is a resin/column, then an anion exchange column must be the resin/column."

elution_question = "What acid is used in the elution during the above reaction?"
elution_example_answer = "Since they say: 'When the eluted was switched to 1 M HCl', then 1 M HCl must be the acid used in the elution."

products_question = "What are the products of the above reaction?"
products_example_answer = "Since they say: 'the ﬁrst band coming out was co-produced cobalt radioisotopes (approximately 1 mL), and the second was the 64Cu, which was collected', and the first and second bands represent products, then cobalt radioisotopes and 64Cu, or Copper-64, must be the products."

target_example = f"Context: {example_context}\n Question: {target_question}\n Answer: {target_example_answer}"
acid_example = f"Context: {example_context}\n Question: {acid_question}\n Answer: {acid_example_answer}"
resin_example = f"Context: {example_context}\n Question: {resin_question}\n Answer: {resin_example_answer}"
elution_example = f"Context: {example_context}\n Question: {elution_question}\n Answer: {elution_example_answer}"
products_example = f"Context: {example_context}\n Question: {products_question}\n Answer: {products_example_answer}"

questions = [target_question, acid_question, resin_question, elution_question, products_question]
questions_examples_dict = {target_question : target_example,
                           acid_question : acid_example,
                           resin_question : resin_example,
                           elution_question : elution_example,
                           products_question : products_example}

answer_questions_dict = {}
answer_context_dict = {}



def calculate_perplexity(model, tokenizer, text):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pt1 = time.perf_counter()
    # Encode the text
    encodings = tokenizer(text, return_tensors='pt').to(device)

    # Define input_ids and target_ids
    input_ids = encodings.input_ids
    target_ids = input_ids.clone()

    with torch.no_grad():
        outputs = model(input_ids, labels=target_ids)

    # Loss calculation
    neg_log_likelihood = outputs.loss

    # Perplexity calculation
    ppl = torch.exp(neg_log_likelihood)
    perp_time = time.perf_counter()-pt1
    print(f"Time to calculate perplexity: {perp_time}")
    return ppl


def load_model(model_name: str):
    """
    This function loads a model from HuggingFace's transformers library to be used for text-generation

    Args:
        model_name (str): A string representing the model as it is reprented in the transformers library.
    
    Returns:
        model: model object from the transformers library
        tokenizer: tokenizer object from the transformers library
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    lt1 = time.perf_counter()
    if "galactica" in model_name:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        if "6.7b" in model_name or "7b" in model_name or "13b" in model_name or "30b" in model_name or "120b" in model_name:
            model = OPTForCausalLM.from_pretrained(model_name, device_map="auto", pad_token_id=tokenizer.eos_token_id, load_in_8bit=True)
        else:
            model = OPTForCausalLM.from_pretrained(model_name, device_map="auto", pad_token_id=tokenizer.eos_token_id).to(device)
    elif "pythia" in model_name:
        tokenizer = AutoTokenizer.from_pretrained(
                model_name,
                revision="step3000",
                cache_dir=f"./{model_name[model_name.index('/')+1:]}/step3000",
                    )
        if "6.7b" in model_name or "7b" in model_name or "13b" in model_name or "30b" in model_name or "120b" in model_name:
            model = GPTNeoXForCausalLM.from_pretrained(
                    model_name,
                    revision="step3000",
                    cache_dir=f"./{model_name[model_name.index('/')+1:]}/step3000",
                    pad_token_id=tokenizer.eos_token_id,
                    load_in_8bit=True
                    )
        else:
            model = GPTNeoXForCausalLM.from_pretrained(
                    model_name,
                    revision="step3000",
                    cache_dir=f"./{model_name[model_name.index('/')+1:]}/step3000",
                    pad_token_id=tokenizer.eos_token_id,
                    ).to(device)
        
    elif "bloom" in model_name:
        tokenizer = BloomTokenizerFast.from_pretrained(model_name)
        if "6.7b" in model_name or "7b" in model_name or "13b" in model_name or "30b" in model_name or "120b" in model_name:
            model = BloomForCausalLM.from_pretrained(model_name, pad_token_id=tokenizer.eos_token_id, load_in_8bit=True)
        else:
            model = BloomForCausalLM.from_pretrained(model_name, pad_token_id=tokenizer.eos_token_id,).to(device)
            
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        if "6.7b" in model_name or "7b" in model_name or "13b" in model_name or "30b" in model_name or "120b" in model_name:
            model = AutoModelForCausalLM.from_pretrained(model_name, pad_token_id=tokenizer.eos_token_id, trust_remote_code=True, load_in_8bit=True)
        else:
            model = AutoModelForCausalLM.from_pretrained(model_name, pad_token_id=tokenizer.eos_token_id, trust_remote_code=True).to(device)
          

    load_time = time.perf_counter()-lt1
    print(f"Time to load model {model_name}: {load_time}")

    return model, tokenizer


def generate(model, tokenizer, input: str, max_new_tokens=50):
    """
    This function takes loads a model from the transformers library, and generates a completion of a given input string.

    Args:
        model_name (str): A string representing the model as it is reprented in the transformers library.
        input (str): A string for the input to the language model to generate a completion of.
        max_new_tokens (int, optional): An int representing the max number of tokens to be generated by the model. Defaults to 50.

    Returns:
        output (str): A string output that is generated by the model.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    input_ids = tokenizer(input, return_tensors="pt").input_ids.to(device)

    outputs = model.generate(input_ids, max_new_tokens=max_new_tokens, pad_token_id=tokenizer.eos_token_id)
    output = tokenizer.decode(outputs[0])
    return output


def get_context(doc_type = "pdf"):
    """
    This function takes a document type and converts documents of those types to a list of contexts.

    Args:
        doc_type (str, optional): A string to determine what types of documents to convert into a list of contexts, either pdf or html. Defaults to pdf.

    Returns:
        context (list): A list of contexts extracted from the documents in either the pdf or html folders. 
    """
    if "pdf" in doc_type:
        return pdf_to_context()
    elif "html" in doc_type:
        return html_to_context()
    else:
        print(f"Invalid doc_type. \nExpected: 'pdf' or 'html'. \nReceived: {doc_type}")
        return []


def default_generate(model_name: str, contexts: list):
    """
    This function uses no filtering or accuracy techniques to act as a base benchmark for other techniques.
    
    The goal of this function is to use a large language model to analyze paragraphs and extract descriptions of chemical separations from chemistry research papers.

    Args:
        model_name (str): A string representing the model as it is reprented in the transformers library.
        contexts (list): A list of different paragraphs from research papers to be used as context for the large language model.

    Returns:
        Tuple: 
            generations: list of the full responses generated by the model (includes context and examples)
            answers: list of answers only generated by the model
            t: float representing the time it took for the function to run
    """
    t1 = time.perf_counter()
    generations = []
    answers = []
    model, tokenizer = load_model(model_name)
    for context in contexts:
        for q in questions:
            example = questions_examples_dict[q]
            input = f"{example}\n Context: {context}\n Question: {q}\n Answer: "
            generation = generate(model, tokenizer, input)
            answer = generation[len(input):]
            # print(f"Answer: {answer} \n")
            answer_questions_dict[answer] = q
            answer_context_dict[answer] = context
            generations.append(generation)
            answers.append(answer)
    t = time.perf_counter() - t1
    print(f"{len(answers)} generations in {t} seconds.")
    return generations, answers, t


def keyword_filter_generate(model_name: str, contexts: list):
    """
    This function uses keyword filtering only to make responses as efficient:
        keyword_filtering: Throws away all context paragraphs that don't contain any keywords specified in the keywords set at the top of the file.

    The goal of this function is to use a large language model to analyze paragraphs and extract descriptions of chemical separations from chemistry research papers.

    Args:
        model_name (str): A string representing the model as it is reprented in the transformers library.
        contexts (list): A list of different paragraphs from research papers to be used as context for the large language model.

    Returns:
        Tuple: 
            generations: list of the full responses generated by the model (includes context and examples)
            answers: list of answers only generated by the model
            t: float representing the time it took for the function to run
    """
    t1 = time.perf_counter()
    generations = []
    answers = []
    model, tokenizer = load_model(model_name)
    for context in contexts:
        if len(set(context.split()).intersection(keywords)) > 0:
            for q in questions:
                example = questions_examples_dict[q]
                input = f"{example}\n Context: {context}\n Question: {q}\n Answer: "
                generation = generate(model, tokenizer, input)
                answer = generation[len(input):]
                # print(f"Answer: {answer} \n")
                answer_questions_dict[answer] = q
                answer_context_dict[answer] = context
                generations.append(generation)
                answers.append(answer)
    t = time.perf_counter() - t1
    print(f"{len(answers)} generations in {t} seconds.")
    return generations, answers, t


def model_filter_generate(model_name: str, contexts: list):
    """
    This function uses model filtering only to be less wasteful in generating responses:
        model_filtering: Asks the model to determine if the context paragraph contains a chemical extraction and continues if 'yes' in generated in the response.

    The goal of this function is to use a large language model to analyze paragraphs and extract descriptions of chemical separations from chemistry research papers.

    Args:
        model_name (str): A string representing the model as it is reprented in the transformers library.
        contexts (list): A list of different paragraphs from research papers to be used as context for the large language model.

    Returns:
        Tuple: 
            generations: list of the full responses generated by the model (includes context and examples)
            answers: list of answers only generated by the model
            t: float representing the time it took for the function to run
    """
    t1 = time.perf_counter()
    generations = []
    answers = []
    model, tokenizer = load_model(model_name)
    for context in contexts:
        c = f"Context: {context}\n Question: Yes or no, does the above context describe a chemical extraction?\n Answer: "
        filter = generate(model, tokenizer, c, max_new_tokens=20)
        answer = filter[len(c):]
        if "Yes" in answer or "yes" in answer:
            for q in questions:
                example = questions_examples_dict[q]
                input = f"{example}\n Context: {context}\n Question: {q}\n Answer: "
                generation = generate(model, tokenizer, input)
                answer = generation[len(input):]
                # print(f"Answer: {answer} \n")
                answer_questions_dict[answer] = q
                answer_context_dict[answer] = context
                generations.append(generation)
                answers.append(answer)
    t = time.perf_counter() - t1
    print(f"{len(answers)} generations in {t} seconds.")
    return generations, answers, t


def keyword_model_generate(model_name: str, contexts: list):
    """
    This function combines two techniques to make responses as accurate as possible:
        keyword_filtering: Throws away all context paragraphs that don't contain any keywords specified in the keywords set at the top of the file.
        model_filtering: Asks the model to determine if the context paragraph contains a chemical extraction and continues if 'yes' in generated in the response.

    The goal of this function is to use a large language model to analyze paragraphs and extract descriptions of chemical separations from chemistry research papers.

    Args:
        model_name (str): A string representing the model as it is reprented in the transformers library.
        contexts (list): A list of different paragraphs from research papers to be used as context for the large language model.

    Returns:
        Tuple: 
            generations: list of the full responses generated by the model (includes context and examples)
            answers: list of answers only generated by the model
            t: float representing the time it took for the function to run
    """
    t1 = time.perf_counter()
    generations = []
    answers = []
    model, tokenizer = load_model(model_name)
    for context in contexts:
        if len(set(context.split()).intersection(keywords)) > 0:
            c = f"Context: {context}\n Question: Yes or no, does the above context describe a chemical extraction?\n Answer: "
            filter = generate(model, tokenizer, c, max_new_tokens=20)
            answer = filter[len(c):]
            if "Yes" in answer or "yes" in answer:
                for q in questions:
                    example = questions_examples_dict[q]
                    input = f"{example}\n Context: {context}\n Question: {q}\n Answer: "
                    generation = generate(model, tokenizer, input)
                    answer = generation[len(input):]
                    # print(f"Answer: {answer} \n")
                    answer_questions_dict[answer] = q
                    answer_context_dict[answer] = context
                    generations.append(generation)
                    answers.append(answer)
    t = time.perf_counter() - t1
    print(f"{len(answers)} generations in {t} seconds.")
    return generations, answers, t


def keyword_model_expert_check_generate(model_name: str, contexts: list):
    """
    This function combines four techniques to make responses as accurate as possible:
        keyword_filtering: Throws away all context paragraphs that don't contain any keywords specified in the keywords set at the top of the file.
        model_filtering: Asks the model to determine if the context paragraph contains a chemical extraction and continues if 'yes' in generated in the response.
        expert_response: Asks the model to respond as if they are an expert at chemistry to try to make the response more accurate.
        check_response: Asks the model to double check their answer by confirming if their response is truthful/accurate.

    The goal of this function is to use a large language model to analyze paragraphs and extract descriptions of chemical separations from chemistry research papers.

    Args:
        model_name (str): A string representing the model as it is reprented in the transformers library.
        contexts (list): A list of different paragraphs from research papers to be used as context for the large language model.

    Returns:
        Tuple: 
            generations: list of the full responses generated by the model (includes context and examples)
            answers: list of answers only generated by the model
            t: float representing the time it took for the function to run
    """
    t1 = time.perf_counter()
    generations = []
    answers = []
    model, tokenizer = load_model(model_name)
    for context in contexts:
        if len(set(context.split()).intersection(keywords)) > 0:
            
            mt1 = time.perf_counter()
            c = f"Context: {context}\n Question: Yes or no, does the above context describe a chemical extraction?\n Answer: "
            filter = generate(model, tokenizer, c, max_new_tokens=20)
            answer = filter[len(c):]
            m_filter_time = time.perf_counter()-mt1
            print(f"Time for model filter: {m_filter_time}")

            if "Yes" in answer or "yes" in answer:
                for q in questions:
                    example = questions_examples_dict[q]
                    input = f"{example}\n Context: {context}\n Question: {q}\n Respond as if you are an expert at chemistry.\n Answer: "
                    gt1 = time.perf_counter()
                    generation = generate(model, tokenizer, input)
                    gen_time = time.perf_counter()-gt1
                    print(f"Time to generate 1 response: {gen_time}")
                    answer = generation[len(input):]
                    # print(f"Answer: {answer} \n")
                    # check = f"In regards to the context, {context}, is it correct to say that the response: {answer} is the correct evaluation of the question: {q} \n Respond yes or no: "
                    check = f"Question: Answer yes or no: is the response, '{answer}' a truthful statement in regards to the context '{context}'? \n Answer:"

                    ct1 = time.perf_counter()
                    gen = generate(model, tokenizer, check, max_new_tokens=20)
                    check_time = time.perf_counter()-ct1
                    print(f"Time to check answer: {check_time}")

                    confirm = gen[len(check):]
                    # print(confirm)
                    answer_questions_dict[answer] = q
                    
                    if "yes" in confirm or "Yes" in confirm:
                        if "no" in confirm or "No" in confirm:
                            pass
                        else:
                            answer_context_dict[answer] = context
                            generations.append(generation)
                            answers.append(answer)
    t = time.perf_counter() - t1
    print(f"{len(answers)} generations in {t} seconds.")
    return generations, answers, t


def write_to_file(model_name: str, context: list, output_name = "keyword_model_expert_check_output.txt", filter = keyword_model_expert_check_generate):
    """
    This function takes a model name and a list of contexts, and writes the output of the generations by that model and context to a txt file with the name 
    specified by the output_name.

    Args:
        model_name (str): A string representing the model as it is reprented in the transformers library.
        context (list): A list of different paragraphs from research papers to be used as context for the large language model.
        output_name (str, optional): The name of the file to write to. Defaults to "keyword_filter_output.txt".
        filter (function, optional): The filter to use in the response generation. Defaults to keyword_filter_generate.
    """
    _gen, _ans, _time = filter(model_name, context)

    _time = round(_time, 2)

    model, tokenizer = load_model(model_name)

    at1 = time.perf_counter()
    perplexity_scores = []
    total_score = 0
    for _ in _ans:
        score = round(calculate_perplexity(model, tokenizer, _).item(), 2)
        total_score+=score
        perplexity_scores.append(score)

    avg_score = total_score/len(perplexity_scores)
    avg_time = time.perf_counter()-at1
    print(f"Time to calculate average perplexity: {avg_time}")


    k = f"Generated {len(_gen)} responses in {_time} seconds with average perplexity score of {round(avg_score, 2)}"
    for i in range(len(_gen)):
        ans_idx = _gen[i].index('Answer:')
        gen = _gen[i][ans_idx:]
        gen = gen[gen.index('Context:'):]
        question_index = gen.index('Question:')
        ans = _ans[i]
        c = answer_context_dict[ans]
        if not (c in k):
            k += "\n\n\n" + gen[:question_index] + "\n"

        q = answer_questions_dict[ans]
        if q == questions[4]:
            k += "\nQuestion: " + q + "\nAnswer:" + ans.split("\n")[0] + f"\nScore: {perplexity_scores[i]}\n"  
        else:
            k += "\nQuestion: " + q + "\nAnswer:" + ans.split("\n")[0] + f"\nScore: {perplexity_scores[i]}\n"

    with open(f"output/{output_name}" if '.txt' in output_name else f"output/{output_name}.txt", "w", encoding="utf-8") as f:
         f.write(k)


def main():
    """
    Testing loop to test all models with all different filters.
    """
    filters = {keyword_model_expert_check_generate, keyword_model_generate, model_filter_generate,
                keyword_filter_generate, default_generate}
   
    models = {"EleutherAI/pythia-2.8b-deduped", "EleutherAI/pythia-1.4b-deduped", "EleutherAI/gpt-neo-2.7B", 
              "EleutherAI/gpt-neo-1.3B", "bigscience/bloom-1b7", "mosaicml/mpt-1b-redpajama-200b-dolly", "tiiuae/falcon-rw-1b",
              "facebook/opt-2.7b", "facebook/opt-1.3b", "facebook/opt-6.7b", "facebook/galactica-1.3b", "facebook/galactica-6.7b",
              "meta-llama/Llama-2-13b-hf", "meta-llama/Llama-2-7b-hf"}
    
    parsers = ["html", "pdf"]

    for parser in parsers:
        t1 = time.perf_counter()
        context = get_context(parser)
        t2 = time.perf_counter()-t1
        print(f"Time to parse context: {t2}")
        for model in models:
            for filter in filters:
                try:
                    print(f"Model: {model} generating with {str(filter)[10:str(filter).index(' at')]} filter with {len(context)*len(questions)} potential generations.")
                    write_to_file(model, context, output_name=f"{str(filter)[10:str(filter).index(' at')]}-{model[model.index('/')+1:]}-{parser}", filter=filter)
                except Exception as e:
                    print(f"Error encountered running {model} with {str(filter)[10: str(filter).index(' at')]} filter.")
                    print(e)
                    continue


def test():

    parser = "html"
    context = get_context(parser)

    relevant_models = {"facebook/opt-6.7b", "facebook/opt-2.7b", "meta-llama/Llama-2-13b-hf", "meta-llama/Llama-2-7b-hf"}
    filters = {keyword_model_expert_check_generate, keyword_model_generate, keyword_filter_generate}
    
    for model in relevant_models:
        for filter in filters:
            try:
                print(f"Model: {model} generating with {str(filter)[10:str(filter).index(' at')]} filter with {len(context)*len(questions)} potential generations.")
                write_to_file(model, context, output_name=f"{str(filter)[10:str(filter).index(' at')]}-{model[model.index('/')+1:]}-{parser}", filter=filter)
            except Exception as e:
                print(f"Error encountered running {model} with {str(filter)[10: str(filter).index(' at')]} filter.")
                print(e)
                continue


if __name__ == "__main__":
     main()
    # test()
