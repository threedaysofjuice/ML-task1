from nltk.stem import WordNetLemmatizer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
import re

# nltk.download('omw-1.4')
# nltk.download('wordnet')
# nltk.download('stopwords')
# nltk.download('punkt')

en_stops = set(stopwords.words('english'))

def reader(numb):
    openfile = r"text_" + numb + ".txt"
    reader = open(openfile)
    text = reader.read()
    text = text.lower()  #Letters to lowercase

    text = re.sub(r"\d+", "", text, flags=re.UNICODE)  #deleting numbers

    text = re.sub(r"[^\w\s]", "", text, flags=re.UNICODE)  #deleting punctuation

    text_tokens = word_tokenize(text)  # tokenization
    text = [word
         for word in text_tokens
            if not word in en_stops]  # deleting stop words

    lemmatizer = WordNetLemmatizer()
    for i in range(len(text)):
        text[i] = lemmatizer.lemmatize(text[i])

    i = 1
    n = 10

    docs = []

    while i<=n:
        docs.append('text_' + str(i) + ".txt")

        i += 1

    # df1 = pd.DataFrame({'Para1': [text],'Para2': [text],'Para3': [text],'Para4': [text],'Para5': [text],'Para6': [text],'Para7': [text],'Para8': [text],'Para9': [text],'Para10': [text]})
    
    tfidf_vectorizer = TfidfVectorizer()
    doc_vec = tfidf_vectorizer.fit_transform(text)
    word = tfidf_vectorizer.get_feature_names()
    df2 = pd.DataFrame(data=doc_vec.toarray().transpose(), index=docs, columns=word)
    # df2.columns = df1.columns

    print(df2)

for i in range(10):
    reader(str(i + 1))



 
