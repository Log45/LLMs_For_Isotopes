from functions import *
from benchmark import *
import torch

# torch.cuda.empty_cache() # use to free gpu memory after each model

def main():
    """
    This file chooses the most relevant filters from functions.py and tests relevant LLMs on those filters with different
    prompting techniques (zero-CoT, one-shot-CoT, two-shot-CoT)
    """
    filters = {keyword_filter_generate, keyword_model_check_generate, keyword_model_expert_check_generate, keyword_model_generate, keyword_model_expert_generate, model_filter_generate}
    models = {"facebook/galactica-1.3b", "facebook/galactica-6.7b", "meta-llama/Llama-2-13b-hf", "meta-llama/Llama-2-7b-hf", "tiiuae/falcon-7b-instruct"}
    parsers = {"html", "pdf"}
    
    for parser in parsers:
        context = get_context(parser)
        for model in models:
            for filter in filters:
                for i in range(0, 3):
                    try:
                        print(f"Model: {model} generating with {str(filter)[10:str(filter).index(' at')]} filter with {len(context)*len(questions)} potential generations using example {i}.")
                        write_to_file(model, context, i, output_name=f"{str(filter)[10:str(filter).index(' at')]}-{model[model.index('/')+1:]}-{parser}-{i}", filter=filter)
                        torch.cuda.empty_cache()
                    except Exception as e:
                        print(f"Error encountered running {model} example {i} with {str(filter)[10: str(filter).index(' at')]} filter.")
                        print(e)
                        continue
                    
    write_to_csv()
    

def makeup_testing():
    filters = {keyword_filter_generate, keyword_model_check_generate, keyword_model_expert_check_generate, keyword_model_generate, keyword_model_expert_generate, model_filter_generate}
    model = "facebook/galactica-6.7b"
    parser = "html"
    
    context = get_context(parser)
    for filter in filters:
        for i in range(0, 3):
            try:
                print(f"Model: {model} generating with {str(filter)[10:str(filter).index(' at')]} filter with {len(context)*len(questions)} potential generations using example {i}.")
                write_to_file(model, context, i, output_name=f"{str(filter)[10:str(filter).index(' at')]}-{model[model.index('/')+1:]}-{parser}-{i}", filter=filter)
                torch.cuda.empty_cache()
            except Exception as e:
                print(f"Error encountered running {model} example {i} with {str(filter)[10: str(filter).index(' at')]} filter.")
                print(e)
                continue
    
    model = "meta-llama/Llama-2-13b-hf"
    for filter in filters:
        for i in range(0, 3):
            try:
                print(f"Model: {model} generating with {str(filter)[10:str(filter).index(' at')]} filter with {len(context)*len(questions)} potential generations using example {i}.")
                write_to_file(model, context, i, output_name=f"{str(filter)[10:str(filter).index(' at')]}-{model[model.index('/')+1:]}-{parser}-{i}", filter=filter)
                torch.cuda.empty_cache()
            except Exception as e:
                print(f"Error encountered running {model} example {i} with {str(filter)[10: str(filter).index(' at')]} filter.")
                print(e)
                continue  
                 
    filter = keyword_model_expert_generate
    models = {"facebook/galactica-1.3b", "meta-llama/Llama-2-7b-hf", "tiiuae/falcon-7b-instruct"}
    for model in models:
        for i in range(0, 3):
            try:
                print(f"Model: {model} generating with {str(filter)[10:str(filter).index(' at')]} filter with {len(context)*len(questions)} potential generations using example {i}.")
                write_to_file(model, context, i, output_name=f"{str(filter)[10:str(filter).index(' at')]}-{model[model.index('/')+1:]}-{parser}-{i}", filter=filter)
                torch.cuda.empty_cache()
            except Exception as e:
                print(f"Error encountered running {model} example {i} with {str(filter)[10: str(filter).index(' at')]} filter.")
                print(e)
                continue
            
            
if __name__ == "__main__":
    makeup_testing()
    write_to_csv()
    