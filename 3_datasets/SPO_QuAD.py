import json
#open 2_webscraping/faq_data.txt
 
# Read the context from faq.txt and faq2.txt
with open('../2_web_scraping/faq_data.txt', 'r', encoding='utf-8') as file:
    context1 = file.read()

with open('../2_web_scraping/faq_data2.txt', 'r', encoding='utf-8') as file:
    context2 = file.read()

# Read the question and answer data from faq_data.json and faq_data2.json
with open('../2_web_scraping/faq_data.json', 'r', encoding='utf-8') as file:
    data1 = json.load(file)

with open('../2_web_scraping/faq_data2.json', 'r', encoding='utf-8') as file:
    data2 = json.load(file)

# Generate the dataset
dataset = {
    "data": [
        {
            "paragraphs": [
                {
                    "context": context1,
                    "document_id": 1,
                    "qas": [
                        {
                            "question": qa["question"],
                            "id": i + 1,
                            "answers": [
                                {
                                    "answer_id": i + 1,
                                    "document_id": 1,
                                    "question_id": i + 1,
                                    "text": qa["answer"],
                                    "answer_start": context1.find(qa["answer"]),
                                    #"answer_category": "SHORT"
                                }
                            ]
                        } for i, qa in enumerate(data1)
                    ]
                },
                {
                    "context": context2,
                    "document_id": 2,
                    "qas": [
                        {
                            "question": qa["question"],
                            "id": i + 1,
                            "answers": [
                                {
                                    "answer_id": i + 1,
                                    "document_id": 2,
                                    "question_id": i + 1,
                                    "text": qa["answer"],
                                    "answer_start": context2.find(qa["answer"]),
                                    #"answer_category": "SHORT"
                                }
                            ]
                        } for i, qa in enumerate(data2)
                    ]
                }
            ]
        }
    ]
}

# Save the dataset to a file
with open('SPO-QuAD.json', 'w', encoding='utf-8') as file:
    json.dump(dataset, file, ensure_ascii=False, indent=4)
