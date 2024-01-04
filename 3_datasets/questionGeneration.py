from openai import OpenAI
import re

client = OpenAI(
  api_key="API_KEY_HERE"
)


def generate_questions(context, n, id, document_id):
    qa = client.completions.create(
        model="text-davinci-003",
        prompt=f"Erstelle {n} Fragen und beantworte sie nur durch wortwörtliches zitieren mit Groß- und Kleinschreibung: {context}. Formatiere die Fragen und Antworten so:  Q1: A1: Q2: A2: ... Achte darauf dass die Antworten Zeichengenau im Text vorkommen,",
        max_tokens=1000,
        #n=n,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(qa.choices[0].text)
    

    # Format questions and answers in SQuAD format
    squad_data = {
        "paragraphs": [
            {
                "context": context,
                "document_id": document_id,
                "qas": []
            }
        ]
    }


    qa_list = re.split(r'(Q\d+: |A\d+: )', qa.choices[0].text)[1:]
    for i in range(0, len(qa_list), 4):
        question = qa_list[i+1].strip()
        answer = qa_list[i+3].strip().replace('"', '')
        answer_start = context.find(answer)
        answer_end = answer_start + len(answer)
        id_qa = id + i//4
        qa_pair = {
            "question": question,
            "id": id_qa,
            "answers": [
                {
                    "answer_id": id_qa,
                    "document_id": document_id,
                    "question_id": id_qa,
                    "text": answer,
                    "answer_start": answer_start,
                    "answer_end": answer_end,
                }
            ],
            "is_impossible": False
        }
        squad_data["paragraphs"][0]["qas"].append(qa_pair)
    
    return squad_data

# Example usage:
context = "Allgemeine Abkürzungen: Sem = Semester, SWS = Semesterwochenstunden, ECTS = European Credit Transfer System, LV = Lehrveranstaltung, MO = Modul, PM = Pflichtmodul, WPM = Wahlpflichtmodul, EN = Englischsprachige Veranstaltung, V = Vorlesung, Ü = Übung (mit Betreuung), LÜ = Laborübung, W = Workshop / Seminar, P = Praktikum, PJ = Projekt, E = Exkursion, X = Veranstaltungsart ist abhängig von der gewählten Veranstaltung, PSS = Integriertes praktisches Studiensemester, TSS = Theoretisches Auslandsstudiensemester"
n = 4
id = 127
document_id = 84

squad_format_data = generate_questions(context, n, id, document_id)

import json

def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


write_json('gptQA.json', squad_format_data)