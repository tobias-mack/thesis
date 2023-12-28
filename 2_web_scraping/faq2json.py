import json

# open the faq_data.txt file
with open("datasets/faq_data.txt", "r") as f:
    lines = f.readlines()

# create a list of dictionaries with the fields "question" and "answer"
data = []
question = ""
answer = ""
for line in lines:
    if line.startswith("Frage: "):
        # if we encounter a new question, add the previous question-answer pair to the data list
        if question and answer:
            data.append({"question": question, "answer": answer})
        # start a new question-answer pair
        question = line[7:].strip()
        answer = ""
    elif line.startswith("Antwort: "):
        # add the answer to the current question-answer pair
        answer += line[9:]
    else:
        # ignore any other lines
        pass

# add the last question-answer pair to the data list
if question and answer:
    data.append({"question": question, "answer": answer})

# write the data to a JSON file
with open("faq_data.json", "w") as f:
    json.dump(data, f)