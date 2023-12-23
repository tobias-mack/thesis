from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained(
    "deepset/gelectra-large-germanquad")
model = AutoModelForQuestionAnswering.from_pretrained(
    "deepset/gelectra-large-germanquad")

tokens = tokenizer.encode('This is a test.', return_tensors='pt')

decoded_tokens = [tokenizer.decode(token.item())
                   for token in tokens[0]]

print("Decoded Tokens:")
for token, decoded_token in zip(tokens[0], decoded_tokens):
    print(f"Token: {token.item()}, Decoded: {decoded_token}")