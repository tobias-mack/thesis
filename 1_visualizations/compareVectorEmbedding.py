import gensim.downloader as api
import matplotlib.pyplot as plt
import numpy as np

wv = api.load('word2vec-google-news-300')

car = wv['car']
minivan = wv['minivan']
cereal = wv['cereal']

cosine_sim = wv.cosine_similarities(car, [minivan, cereal])
print(cosine_sim)

car = car.reshape(-1, 1)
minivan = minivan.reshape(-1, 1)
cereal = cereal.reshape(-1, 1)

my_cmap = plt.get_cmap("viridis")
rescale = lambda y: (y - np.min(y)) / (np.max(y) - np.min(y))

fig, axs = plt.subplots(3, 1)  # Create 2 subplots

axs[0].bar(np.arange(50, 90), height=0.03, width=1, bottom=0, color=my_cmap(rescale(car[50:90,0])))
axs[1].bar(np.arange(50, 90), height=0.03, width=1, bottom=0, color=my_cmap(rescale(minivan[50:90,0])))
axs[2].bar(np.arange(50, 90), height=0.03, width=1, bottom=0, color=my_cmap(rescale(cereal[50:90,0])))
axs[0].set_ylabel('car') 
axs[1].set_ylabel('minivan')
axs[2].set_ylabel('cereal') 
axs[0].set_yticks([])
axs[1].set_yticks([])
axs[2].set_yticks([])

plt.show()