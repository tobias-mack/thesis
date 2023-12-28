import gradio as gr

# DOCUMENT LOADING
from haystack.nodes import TextConverter

converter = TextConverter(remove_numeric_tables=True, valid_languages=["de"])
path="datasets/faq_data.txt"
docs = converter.convert(file_path=path, meta=None)

# DOCUMENT SPLITTING

from haystack.nodes import PreProcessor

preprocessor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=False,
    split_by="word",
    split_length=500,
    split_respect_sentence_boundary=True,
)
docs_default = preprocessor.process(docs)


from haystack.document_stores import InMemoryDocumentStore

# Setup Document Store
document_store = InMemoryDocumentStore(use_bm25=True)
document_store.write_documents(docs_default)

from haystack.nodes import BM25Retriever

# Initialize Retriever
retriever = BM25Retriever(document_store=document_store)

# RETRIEVAL
from haystack.pipelines import DocumentSearchPipeline
from haystack.utils import print_documents


# Initialize QA-Pipeline
from haystack.pipelines import ExtractiveQAPipeline
from haystack.nodes import FARMReader

import torch
print("GRAFIKKARTE: " + str(torch.cuda.is_available()))


reader = FARMReader(model_name_or_path="deepset/gelectra-large-germanquad", use_gpu=True)
pipe = ExtractiveQAPipeline(reader, retriever)

n_retriever_results = 3
n_answers = 3

def answer_question(question):
    prediction = pipe.run(query=question, params={"Retriever": {"top_k": n_retriever_results}, "Reader": {"top_k": n_answers}})
    answers = prediction["answers"]
    if answers:
        for ans in range(0, n_answers):
            if answers[ans].answer != "":
                print(answers[ans].answer)
        return answers[0].answer 
    else: 
        return "No answer found"

iface = gr.Interface(fn=answer_question, inputs="text", outputs="text")
iface.launch()