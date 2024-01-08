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

text-embedding-ada-002
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

sentence-transformers/distiluse-base-multilingual-cased-v1
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

query_embedding_model = deepset/gbert-base-germandpr-question_encoder
passage_embedding_model = deepset/gbert-base-germandpr-ctx_encoder
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
  

text-embedding-ada-002
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

sentence-transformers/distiluse-base-multilingual-cased-v1
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

query_embedding_model = deepset/gbert-base-germandpr-question_encoder
passage_embedding_model = deepset/gbert-base-germandpr-ctx_encoder
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

text-embedding-ada-002
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

sentence-transformers/distiluse-base-multilingual-cased-v1
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


query_embedding_model = deepset/gbert-base-germandpr-question_encoder
passage_embedding_model = deepset/gbert-base-germandpr-ctx_encoder
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

```
Colab Environment
GPU:T4 15GB VRAM
RAM:51GB
====================================================
deepset/gelectra-large-germanquad 
====================================================
ISOLATED
{'Retriever': {},
 'Reader': {'exact_match': 0.015873015873015872,
  'f1': 0.3927590607601699,
  'sas': 0.7107437252998352,
  'num_examples_for_eval': 63.0}}

text-embedding-ada-002
{'Retriever': {'recall_multi_hit': 1.0,
  'recall_single_hit': 1.0,
  'precision': 0.1999999999999999,
  'map': 0.9735449735449735,
  'mrr': 0.9735449735449735,
  'ndcg': 0.9803469763038558},
 'Reader': {'exact_match': 0.015873015873015872,
  'f1': 0.41259693123114444,
  'sas': 0.7148523330688477,
  'num_examples_for_eval': 63.0}}
  
BM25
{'Retriever': {'recall_multi_hit': 1.0,
  'recall_single_hit': 1.0,
  'precision': 0.1999999999999999,
  'map': 0.9761904761904762,
  'mrr': 0.9761904761904762,
  'ndcg': 0.9824252263605456},
 'Reader': {'exact_match': 0.015873015873015872,
  'f1': 0.40894137924626317,
  'sas': 0.7126258015632629,
  'num_examples_for_eval': 63.0}}

sentence-transformers/distiluse-base-multilingual-cased-v1
{'Retriever': {'recall_multi_hit': 0.8571428571428571,
  'recall_single_hit': 0.8571428571428571,
  'precision': 0.17142857142857137,
  'map': 0.6894179894179894,
  'mrr': 0.6894179894179894,
  'ndcg': 0.7306380363741704},
 'Reader': {'exact_match': 0.015873015873015872,
  'f1': 0.3850290569231127,
  'sas': 0.6994900703430176,
  'num_examples_for_eval': 63.0}}

query_embedding_model = deepset/gbert-base-germandpr-question_encoder
passage_embedding_model = deepset/gbert-base-germandpr-ctx_encoder
{'Retriever': {'recall_multi_hit': 0.6031746031746031,
  'recall_single_hit': 0.6031746031746031,
  'precision': 0.12063492063492066,
  'map': 0.44206349206349205,
  'mrr': 0.44206349206349205,
  'ndcg': 0.48204914874482546},
 'Reader': {'exact_match': 0.015873015873015872,
  'f1': 0.31987626447686596,
  'sas': 0.6675589680671692,
  'num_examples_for_eval': 63.0}}


====================================================
deutsche-telekom/bert-multi-english-german-squad2
====================================================
ISOLATED
{'Retriever': {},
 'Reader': {'exact_match': 0.0,
  'f1': 0.1928264819195505,
  'sas': 0.6431787610054016,
  'num_examples_for_eval': 63.0}}

text-embedding-ada-002
{'Retriever': {'recall_multi_hit': 1.0,
  'recall_single_hit': 1.0,
  'precision': 0.1999999999999999,
  'map': 0.9735449735449735,
  'mrr': 0.9735449735449735,
  'ndcg': 0.9803469763038558},
 'Reader': {'exact_match': 0.0,
  'f1': 0.22992581015272573,
  'sas': 0.6542592644691467,
  'num_examples_for_eval': 63.0}}
  
BM25
{'Retriever': {'recall_multi_hit': 1.0,
  'recall_single_hit': 1.0,
  'precision': 0.1999999999999999,
  'map': 0.9761904761904762,
  'mrr': 0.9761904761904762,
  'ndcg': 0.9824252263605456},
 'Reader': {'exact_match': 0.0,
  'f1': 0.21997046373900941,
  'sas': 0.6510328650474548,
  'num_examples_for_eval': 63.0}}

sentence-transformers/distiluse-base-multilingual-cased-v1
{'Retriever': {'recall_multi_hit': 0.8571428571428571,
  'recall_single_hit': 0.8571428571428571,
  'precision': 0.17142857142857137,
  'map': 0.6894179894179894,
  'mrr': 0.6894179894179894,
  'ndcg': 0.7306380363741704},
 'Reader': {'exact_match': 0.0,
  'f1': 0.1999092572905283,
  'sas': 0.6401894688606262,
  'num_examples_for_eval': 63.0}}

query_embedding_model = deepset/gbert-base-germandpr-question_encoder
passage_embedding_model = deepset/gbert-base-germandpr-ctx_encoder
{'Retriever': {'recall_multi_hit': 0.6031746031746031,
  'recall_single_hit': 0.6031746031746031,
  'precision': 0.12063492063492066,
  'map': 0.44206349206349205,
  'mrr': 0.44206349206349205,
  'ndcg': 0.48204914874482546},
 'Reader': {'exact_match': 0.0,
  'f1': 0.17978284148634666,
  'sas': 0.6212383508682251,
  'num_examples_for_eval': 63.0}}
====================================================
gpt-3.5-turbo-1106
====================================================
ISOLATED
{'Retriever': {}, 'Reader': {}}

text-embedding-ada-002
{'Retriever': {'recall_multi_hit': 1.0,
  'recall_single_hit': 1.0,
  'precision': 0.1999999999999999,
  'map': 0.9735449735449735,
  'mrr': 0.9735449735449735,
  'ndcg': 0.9803469763038558},
 'Reader': {'exact_match': 0.0,
  'f1': 0.3572332237629609,
  'sas': 0.721752405166626,
  'num_examples_for_eval': 63.0}}
  
BM25
{'Retriever': {'recall_multi_hit': 1.0,
  'recall_single_hit': 1.0,
  'precision': 0.1999999999999999,
  'map': 0.9761904761904762,
  'mrr': 0.9761904761904762,
  'ndcg': 0.9824252263605456},
 'Reader': {'exact_match': 0.0,
  'f1': 0.36503612012505704,
  'sas': 0.7207269072532654,
  'num_examples_for_eval': 63.0}}

sentence-transformers/distiluse-base-multilingual-cased-v1
{'Retriever': {'recall_multi_hit': 0.8571428571428571,
  'recall_single_hit': 0.8571428571428571,
  'precision': 0.17142857142857137,
  'map': 0.6894179894179894,
  'mrr': 0.6894179894179894,
  'ndcg': 0.7306380363741704},
 'Reader': {'exact_match': 0.0,
  'f1': 0.3450613395982281,
  'sas': 0.7186266779899597,
  'num_examples_for_eval': 63.0}}


query_embedding_model = deepset/gbert-base-germandpr-question_encoder
passage_embedding_model = deepset/gbert-base-germandpr-ctx_encoder
{'Retriever': {'recall_multi_hit': 0.6031746031746031,
  'recall_single_hit': 0.6031746031746031,
  'precision': 0.12063492063492066,
  'map': 0.44206349206349205,
  'mrr': 0.44206349206349205,
  'ndcg': 0.48204914874482546},
 'Reader': {'exact_match': 0.0,
  'f1': 0.323787612175441,
  'sas': 0.6868749856948853,
  'num_examples_for_eval': 63.0}}

```