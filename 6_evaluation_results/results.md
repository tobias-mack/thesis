# Results

## Evaluation on SPO Dataset

```
Colab Environment
GPU:T4 15GB VRAM
RAM:51GB
====================================================
deepset/gelectra-large-germanquad 
====================================================
ISOLATED
{'Retriever': {},
 'Reader': {'exact_match': 0.25757575757575757,
  'f1': 0.6108242913878609,
  'sas': 0.7283448576927185,
  'num_examples_for_eval': 66.0}}

OPENAI
{'Retriever': {'recall_multi_hit': 0.9848484848484849,
  'recall_single_hit': 0.9848484848484849,
  'precision': 0.21212121212121207,
  'map': 0.8962962962962963,
  'mrr': 0.8987373737373737,
  'ndcg': 0.9193991660495363},
 'Reader': {'exact_match': 0.2727272727272727,
  'f1': 0.6203552049755567,
  'sas': 0.7426201105117798,
  'num_examples_for_eval': 66.0}}
  
BM25
{'Retriever': {'recall_multi_hit': 0.9242424242424242,
  'recall_single_hit': 0.9242424242424242,
  'precision': 0.2265151515151515,
  'map': 0.8181818181818182,
  'mrr': 0.8232323232323232,
  'ndcg': 0.8462945979136431},
 'Reader': {'exact_match': 0.24242424242424243,
  'f1': 0.582451374626288,
  'sas': 0.7183138132095337,
  'num_examples_for_eval': 66.0}}

sentence-transformer
{'Retriever': {'recall_multi_hit': 0.9393939393939394,
  'recall_single_hit': 0.9393939393939394,
  'precision': 0.19999999999999996,
  'map': 0.7719696969696969,
  'mrr': 0.7757575757575758,
  'ndcg': 0.8153600375479062},
 'Reader': {'exact_match': 0.25757575757575757,
  'f1': 0.6051150905605626,
  'sas': 0.7355108261108398,
  'num_examples_for_eval': 66.0}}

DPR
{'Retriever': {'recall_multi_hit': 0.6515151515151515,
  'recall_single_hit': 0.6515151515151515,
  'precision': 0.13939393939393938,
  'map': 0.4247474747474747,
  'mrr': 0.42424242424242425,
  'ndcg': 0.48158554148542176},
 'Reader': {'exact_match': 0.19696969696969696,
  'f1': 0.5039852972452163,
  'sas': 0.6740997433662415,
  'num_examples_for_eval': 66.0}}


====================================================
deutsche-telekom/bert-multi-english-german-squad2
====================================================
ISOLATED
{'Retriever': {},
 'Reader': {'exact_match': 0.12121212121212122,
  'f1': 0.4763148378019208,
  'sas': 0.6490762233734131,
  'num_examples_for_eval': 66.0}}
  

OPENAI
{'Retriever': {'recall_multi_hit': 0.9848484848484849,
  'recall_single_hit': 0.9848484848484849,
  'precision': 0.21212121212121207,
  'map': 0.8962962962962963,
  'mrr': 0.8987373737373737,
  'ndcg': 0.9193991660495363},
 'Reader': {'exact_match': 0.12121212121212122,
  'f1': 0.4762624476548019,
  'sas': 0.66419917345047,
  'num_examples_for_eval': 66.0}}
  
BM25
{'Retriever': {'recall_multi_hit': 0.9242424242424242,
  'recall_single_hit': 0.9242424242424242,
  'precision': 0.2265151515151515,
  'map': 0.8181818181818182,
  'mrr': 0.8232323232323232,
  'ndcg': 0.8462945979136431},
 'Reader': {'exact_match': 0.10606060606060606,
  'f1': 0.4479858225903751,
  'sas': 0.6469358801841736,
  'num_examples_for_eval': 66.0}}

sentence-transformer
{'Retriever': {'recall_multi_hit': 0.9393939393939394,
  'recall_single_hit': 0.9393939393939394,
  'precision': 0.19999999999999996,
  'map': 0.7719696969696969,
  'mrr': 0.7757575757575758,
  'ndcg': 0.8153600375479062},
 'Reader': {'exact_match': 0.12121212121212122,
  'f1': 0.4788714525621552,
  'sas': 0.6676162481307983,
  'num_examples_for_eval': 66.0}}

DPR
{'Retriever': {'recall_multi_hit': 0.6515151515151515,
  'recall_single_hit': 0.6515151515151515,
  'precision': 0.13939393939393938,
  'map': 0.4247474747474747,
  'mrr': 0.42424242424242425,
  'ndcg': 0.48158554148542176},
 'Reader': {'exact_match': 0.12121212121212122,
  'f1': 0.4264667549928238,
  'sas': 0.6194432973861694,
  'num_examples_for_eval': 66.0}}
====================================================
gpt-3.5-turbo-1106
====================================================
ISOLATED (sadly not possible with PromptNode at the moment)
{'Retriever': {}, 'Reader': {}}

OPENAI
{'Retriever': {'recall_multi_hit': 0.9848484848484849,
  'recall_single_hit': 0.9848484848484849,
  'precision': 0.21212121212121207,
  'map': 0.8962962962962963,
  'mrr': 0.8987373737373737,
  'ndcg': 0.9193991660495363},
 'Reader': {'exact_match': 0.09090909090909091,
  'f1': 0.48665190580758505,
  'sas': 0.7115304470062256,
  'num_examples_for_eval': 66.0}}
  
BM25
{'Retriever': {'recall_multi_hit': 0.9242424242424242,
  'recall_single_hit': 0.9242424242424242,
  'precision': 0.2265151515151515,
  'map': 0.8181818181818182,
  'mrr': 0.8232323232323232,
  'ndcg': 0.8462945979136431},
 'Reader': {'exact_match': 0.06060606060606061,
  'f1': 0.4475509703113666,
  'sas': 0.7061960697174072,
  'num_examples_for_eval': 66.0}}

sentence-transformer
{'Retriever': {'recall_multi_hit': 0.9393939393939394,
  'recall_single_hit': 0.9393939393939394,
  'precision': 0.19999999999999996,
  'map': 0.7719696969696969,
  'mrr': 0.7757575757575758,
  'ndcg': 0.8153600375479062},
 'Reader': {'exact_match': 0.06060606060606061,
  'f1': 0.4412552743443995,
  'sas': 0.6940531730651855,
  'num_examples_for_eval': 66.0}}


DPR
{'Retriever': {'recall_multi_hit': 0.6515151515151515,
  'recall_single_hit': 0.6515151515151515,
  'precision': 0.13939393939393938,
  'map': 0.4247474747474747,
  'mrr': 0.42424242424242425,
  'ndcg': 0.48158554148542176},
 'Reader': {'exact_match': 0.015151515151515152,
  'f1': 0.36988675396698484,
  'sas': 0.6621365547180176,
  'num_examples_for_eval': 66.0}}

```


## Evaluation on FAQ Dataset
