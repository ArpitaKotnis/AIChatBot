from models.model_load import load_model

model, tokenizer = load_model()
chat_history = ""

def get_response(user_input):
    global chat_history
    chat_history += f"User: {user_input}\nAI:"
    input_ids = tokenizer.encode(chat_history, return_tensors="pt")
    output = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    chat_history += response + "\n"
    return response
