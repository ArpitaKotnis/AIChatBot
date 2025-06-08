from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    return model, tokenizer
