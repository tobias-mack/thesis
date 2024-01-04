import json
import os

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Read the two JSON files
file1_data = read_json('../2_web_scraping/faq_data.json')
file2_data = read_json('../2_web_scraping/faq_data2.json')

# Combine the data from the two files
combined_data = file1_data + file2_data

# Initialize counters
id_counter = 1
document_id_counter = 1

# Prepare the new data in the SQuAD format
squad_data = {
    "data": [
        {
            "title": "FAQ",
            "paragraphs": [
                {
                    "context": item['question'] + ' ' + item['answer'],
                    "qas": [
                        {
                            "question": item['question'],
                            "id": str(id_counter),
                            "answers": [
                                {
                                    "answer_id": str(id_counter),
                                    "document_id": str(id_counter),
                                    "question_id": str(id_counter),
                                    "text": item['answer'],
                                    "answer_start": (item['question'] + ' ' + item['answer']).index(item['answer']),
                                    "answer_end": (item['question'] + ' ' + item['answer']).index(item['answer']) + len(item['answer'])
                                }
                            ],
                            "is_impossible": False
                        }
                    ]
                } for id_counter, item in enumerate(combined_data, start=1)
            ]
        }
    ]
}


# Write the new data into a new JSON file
write_json('faq_SQuAD.json', squad_data)