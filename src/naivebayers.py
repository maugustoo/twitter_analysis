import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict


dataset = pd.read_csv('./final_racism/final_all.csv')

tweets = dataset['text'].values
classes = dataset['is_racism'].values

vectorizer = CountVectorizer(analyzer="word")
#vectorizer = CountVectorizer(ngram_range=(1,2))

freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets, classes)

resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)

print(metrics.accuracy_score(classes, resultados))


testes = ['Ah, vsf esse preto inutil',
         'Lá vem o cara falando merda',
         'Denegrir?? Sério??',
         'negrinho escroto mano, pra que isos?',
         'denegrir a gente']

freq_testes = vectorizer.transform(testes)
print(modelo.predict(freq_testes))
