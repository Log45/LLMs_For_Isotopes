from functions import *
from benchmark import *
import torch

torch.cuda.empty_cache() # use to free gpu memory after each model

def main():
    filters = {keyword_filter_generate, keyword_model_check_generate, keyword_model_expert_check_generate, keyword_model_generate, keyword_model_expert_generate, model_filter_generate}
    models = {"facebook/galactica-1.3b", "facebook/galactica-6.7b",
              "meta-llama/Llama-2-13b-hf", "meta-llama/Llama-2-7b-hf", }
    parsers = {"html", "pdf"}
    
    
    torch.cuda.empty_cache()