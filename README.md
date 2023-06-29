This is a repository with all of my research for the SULI program Summer 2023.


## Models to use:
- Galactica (galai) https://arxiv.org/abs/2211.09085 
- LLaMA (openllama) https://arxiv.org/abs/2302.13971 
    - Find version that is trained from scratch rather than using LLaMA Tokenizer
- MPT(try storywriter) https://www.mosaicml.com/blog/mpt-7b 
    - Because of memory issues, instead testing MPT-1b
- Falcon 40B (7B version available)?  *it’s really slow right now* https://huggingface.co/TheBloke/falcon-40b-instruct-GPTQ 
    - Just like with MPT, instead using 1b version
    - https://huggingface.co/tiiuae/falcon-7b-instruct 
    - https://huggingface.co/tiiuae/falcon-7b 
    - https://www.youtube.com/watch?v=KenORQDCXV0 
    - There is no paper for this model yet it’s that new. 
    - Supposedly better than MPT-7B but really slow
    - Falcon-RW-1B https://arxiv.org/abs/2306.01116 
- BLOOM https://arxiv.org/abs/2211.05100 
    - https://huggingface.co/docs/transformers/model_doc/bloom 
- OPT https://arxiv.org/abs/2205.01068 
- Pythia


## Other relevant papers:
- Universal Distillation code: https://github.com/iPieter/universal-distillation 
- Prompt Surrogate: https://github.com/keirp/automatic_prompt_engineer/blob/main/demo.ipynb 
- AutoPrompt: Eliciting Knowledge from Language Models with Automatically Generated Prompts https://arxiv.org/abs/2010.15980 
- Prefix-Tuning: Optimizing Continuous Prompts for Generation https://arxiv.org/abs/2101.00190 
- The Power of Scale for Parameter-Efficient Prompt Tuning https://arxiv.org/abs/2104.08691 
- Scaling Laws for Neural Language Models
    - https://arxiv.org/abs/2001.08361 
- Scaling Laws for Generative Mixed-Modal Language Models
    - https://arxiv.org/abs/2301.03728 
- Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation 
    - https://arxiv.org/abs/2108.12409 
- Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes
    - https://arxiv.org/abs/2305.02301 
    - New process for distilling models
- ***SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models***
    - https://arxiv.org/abs/2211.10438 
    - https://github.com/mit-han-lab/smoothquant 
    - USE THIS TO GET MODELS THAT DON’T EAT MEMORY (OPT-6.7b)

## Chemistry Papers:
- Actinide speciation in the environment
    - https://akjournals.com/configurable/content/journals$002f10967$002f273$002f3$002farticle-p695.xml?t:ac=journals%24002f10967%24002f273%24002f3%24002farticle-p695.xml 

## Information Extraction Papers:
- Extracting Accurate Materials Data from Research Papers with Conversational Language Models and Prompt Engineering -- Example of ChatGPT
    https://arxiv.org/abs/2303.05352 
    Uses a prompt framework to more reliably extract data from papers

- Match-Prompt: Improving Multi-task Generalization Ability for Neural Text Matching via Prompt Learning
    - https://dl.acm.org/doi/abs/10.1145/3511808.3557388 
    - This doesn’t seem to be towards prompt engineering of LLMs, more on PLMs (it seems like there’s a difference)
    - PLM: Pre-trained Language Model

- Decorate the Examples: A Simple Method of Prompt Design for Biomedical Relation Extraction
    - https://arxiv.org/abs/2204.10360 
    - Useful if we want to extract info on relations between chemicals

- A Unified Generative Framework based on Prompt Learning for Various Information Extraction Tasks
    - https://arxiv.org/abs/2209.11570 
    - Framework that helps LLMs produce more consistent responses; not immediately used for research but may be able to be adapted.

- KnowPrompt: Knowledge-aware Prompt-tuning with Synergistic Optimization for Relation Extraction
    - https://dl.acm.org/doi/abs/10.1145/3485447.3511998 
    - May be useful 

- Relation Extraction as Open-book Examination: Retrieval-enhanced Prompt Tuning
    - https://dl.acm.org/doi/abs/10.1145/3477495.3531746 
    - Talks a lot about PLMs
    - Didn’t completely understand from my skimming of the paper
    - Seems like it may be useful if same applies to LLMs

- BioKnowPrompt: Incorporating imprecise knowledge into prompt-tuning verbalizer with biomedical text for relation extraction
    - https://www.sciencedirect.com/science/article/pii/S0020025522011860 
    - If adapted from Biology to Chemistry this can be useful

## WSL/Ubuntu Setup Instructions:
Download WSL through powershell using command: https://learn.microsoft.com/en-us/windows/wsl/install

`wsl --install`

Once WSL is installed and Ubuntu is setup:
    - Restart for it to take effect
    - Open wsl in powershell using:

`wsl`

Begin setting up anaconda: https://www.hostinger.com/tutorials/how-to-install-anaconda-on-ubuntu/ 
    - Run the following commands from your Linux distro:

`sudo apt-get update`

`cd /tmp`
`apt-get install wget`
`wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh`
`sha256sum Anaconda3-2023.03-1-Linux-x86_64.sh`
`bash Anaconda3-2023.03-1-Linux-x86_64.sh`

Navigate through the Anaconda setup, choose an install directory and then test the connection with the following commands:

`source ~/.bashrc`
`conda info`

Once conda is working in your Ubuntu shell, create a new conda environment using:

`conda create -n env_name`

If you want to choose a specific version of python in the environment, then you can run the command:

`conda install python=X.XX` (X.XX is the python version)
**For our use case, we need Python 3.8 or 3.9 to be compatible with galai

Next, install libraries that may be necessary, for this project: PyTorch, numpy, matplotlib, git, jupyter, galai (or LLaMA depending on which route we choose):

(Python libraries can be install with either pip or conda)

`conda install torchvision torchaudio pytorch-cuda=11.7 git -c pytorch -c nvidia`
`conda install jupyter`
`pip install matplotlib`
`pip install galai`

For more on how to use galai: https://github.com/paperswithcode/galai 
https://tmmtt.medium.com/getting-started-with-galactica-language-model-b380a406ee9f 
https://towardsai.net/p/l/how-to-access-scientific-knowledge-with-galactica 

For creating an env with LLaMA, follow this guide: https://levelup.gitconnected.com/how-to-run-your-own-llama-550cd69b1bc9 

## Prompting Techniques   

https://www.promptingguide.ai/techniques
(All of these tecniques were found at the link above)

### *Zero-Shot Prompting*

- Providing no examples for the LLM besides the context and instruction.

Example Input:
Classify the text into neutral, negative or positive.
Text: I think the vacation is okay.
Sentiment:

### *Few-Show Prompting*

- Providing demonstrations of the format / expected output from the LLM
	
Example input 1:

This is awesome! // Negative
This is bad! // Positive
Wow that movie was rad! // Positive
What a horrible show! //

Example input 2:

A "whatpu" is a small, furry animal native to Tanzania. An example of a sentence that uses the word whatpu is:
We were traveling in Africa and we saw these very cute whatpus.

To do a "farduddle" means to jump up and down really fast. An example of a sentence that uses the word farduddle is:

- Few-Shot prompting is often not enough to get reliable responses for reasoning problems, for that, it would be better to do other prompting techniques below like Chain-of-Thought prompting.

### *Chain-of-Thought Prompting (CoT)*

- Enables complex reasoning capabilities through intermediate reasoning steps.
- Can be combined with few-shot prompting for better results
- https://arxiv.org/abs/2201.11903 
- CoT does not have to be combined with Few-Shot reasoning, there are cases (like below) where Zero-shot-CoT can produce decent reasoning, it is important to remember the case-by-case nature of it. 
- https://arxiv.org/abs/2205.11916

### *Automatic Chain-of-Thought (Auto-CoT)*

- It has been found that generating reasoning chains can still end up with mistakes, so Auto-CoT was developed
- Auto-CoT samples questions with diversity and generates reaosning chains to construct the demonstrations in the following steps.
    1. Question Clustering
        - Partition questions of a given dataset into a few clusters
    2. Demonstration Sampling
        - Select a representative question from each cluster and generate its reasoning chain using Zero-Shot-CoT with simple heuristics
- Simple heuristics involving length of questions and number of steps in rationale encourages the model to use simple and accurate demonstrations.
- https://arxiv.org/abs/2210.03493 
- Code: https://github.com/amazon-science/auto-cot 

### *Self-Consistency* 
- https://arxiv.org/abs/2203.11171
- One of the more advanced techniques
- Aims “to replace the naive greedy decoding used in chain-of-thought prompting”
- Sample multiple, diverse reasoning paths through few-shot CoT and use the generations to select the most consistent answer. 
- Boosts the performance of CoT with arithmetic and commonsense reasoning.
- Examples: https://www.promptingguide.ai/techniques/consistency 

### *Generative Knowledge Prompting* 
- https://arxiv.org/pdf/2110.08387.pdf
- Attempts to generate knowledge to be used as part of the prompt
    - Few-shot prompt with the format of “Input: … Knowledge: …”
    - Eventually generates knowledge relevant to your question
    - Prompts further with the format: “Question: … Knowledge: … Explain and Answer: “
    - The knowledge in the prompt above should be the knowledge previously generated by the AI, which will then have better reasoning in answering your question.

### *Tree of Thoughts (ToT)* 
- https://arxiv.org/abs/2305.10601
- A framework that generalized over chain-of-thought prompting and encourages exploration over thoughts that serve as intermediate steps for general problem solving with language models
- Meant for complex tasks that require exploration or strategic lookahead
- Maintains a tree of thoughts that represent coherent language sequences that serve as intermediate steps toward solving a problem
- Combines thought evaluation and generation with search algorithms to explore thoughts
- Read paper above for more information

### *Automatic Reasoning and Tool-use (ART)*
- https://arxiv.org/abs/2303.09014
- Framework that uses a frozen LLM to automatically generate intermediate reasoning steps as a program.
- How ART works:
    - Given a new task, it selects demonstrations of multi-step reasoning and tool use from a task library
    - At test time, it pauses generation whenever external tools are called, and integrate their output before resuming generation
- Encourages the model to generalize from demonstrations to decompose a new task and use tools in appropriate places in a zero shot fashion.
- Allows humans to fix mistake sin the reasoning steps or add new tools by updating the task and tool libraries.
- See more in the paper linked above. 

### *Automatic Prompt Engineer (APE)*
- https://arxiv.org/abs/2211.01910
- A framework for automatic instruction generation and selection.
- Frames as natural language synthesis addressed as a black-box optimization problem using LLMs to generate and search over candidate solutions.
- First step involves an LLM as an inference model that is given output demonstrations to generate instruction candidates for a task which will guide the search procedure.
- Instructions are executed using a target model.
- The best instruction is selected based on evaluation scores.
    - This enabled researchers to discover a better zero-shot CoT prompt than the previous best: “Let’s think step by step”
    - “Let’s work this out in a step by step way to be sure we have the right answer.”
- More on automatically optimizing prompts:
    - AutoPrompt: proposes an approach to automatically create prompts for a diverse set of tasks based on gradient-guided search. https://arxiv.org/abs/2010.15980 
    - Prefix Tuning: lightweight alternative to fine-tuning that preprends a trainable continuous prefix for NLG tasks. https://arxiv.org/abs/2101.00190 
    - Prompt Tuning: proposes a mechanism for learning soft prompts through backpropogation. https://arxiv.org/abs/2104.08691 

### *Active-Prompt*
- https://arxiv.org/pdf/2302.12246.pdf
- Approach to adapt LLMs to different task-specific example prompts
- First queries the LLM with or without a few CoT examples.
- k possible answers are generated for a set of training questions.
- An uncertainty metric is calculated based on the k answers.
- Most uncertain questions are selected for annotation by humans.
- Those annotated exemplars are used to infer each question. 

### *Directional Stimulus Prompting*
- https://arxiv.org/abs/2302.11520
- Tuneable policy LM trained to generate the stimulus.
- This LM is optimized and generates the hints used to guide a black-box frozen LLM.

### *ReAct*
- https://arxiv.org/abs/2210.03629
- LLMs are used to generate both reasoning traces and task-specific actions in an interleaved manner.
- Reasoning trace allows model to induce, track, update action plans, and handle exceptions.
- Action allows model to interface with and gather information from external sources like knowledge bases or environments. 
- Allows LLMs to interact with external tools to retrieve additional information that leads to more reliable responses.
- (Best approach uses ReAct combined with CoT that allows use of both internal knowledge and external information obtained during reasoning.)
- ReAct allows model to generate task solving trajectories.
- Can retrieve information to support reasoning, while reasoning helps to target what to retrieve next. 
- Since ReAct depends a lot on information it’s retrieving, non-informative search results derails the model reasoning and leads to difficulty in recovering and reformulating thoughts.
- Read about one use-case at: https://python.langchain.com/en/latest/modules/agents/getting_started.html 

### *Multimodal CoT* 
- https://arxiv.org/abs/2302.00923 
- Incorporates text and vision into a two-stage framework
- First step involves rationale gneration based on multimodal information.
- Second step uses answer inference to leverage the informative generated rationals.
- More reading: https://arxiv.org/abs/2302.14045 

### *Graph Prompting*
- https://arxiv.org/abs/2302.08043 
- New prompting framework for graphs to improve performance on downstream task.
