from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd
import pickle
import string
import json
import random
import os


def load_data(raw=None):
    """ load data to development workspaces

    Parameters
    --------------
        raw: (bool) if True, function returns cleaned dataset.
        return (df) data frame of data and its labels
    """
    raw_data = []
    with open('./data/cyber_data.json') as f:
        for line in f:
            raw_data.append(json.loads(line))

    labels = [int(d['annotation']['label'][0]) for d in raw_data]
    text = [d['content'] for d in raw_data]
    data = {'text': text, 'label': labels}
    df = pd.DataFrame(data, columns=['text', 'label'])  # raw data frame

    if raw:
        return df
    else:
        df.text = df.text.apply(clean_text)
        return df


def clean_text(text):
    """ clean input text for the prediction model

    Parameters
    -------------
        text: (str) text to clean
        return (str) post-processed clean text
    """
    lemmatizer = WordNetLemmatizer()
    punctuation = list(string.punctuation)
    punctuation.extend(['.', "’", ','])
    text = BeautifulSoup(text, 'html.parser').text
    filtered_text = ' '.join([word.lower() for word in text.split() if word not in stopwords.words('english')])
    filtered_text = ''.join([c for c in filtered_text if c not in punctuation])
    filtered_text = ''.join([c for c in filtered_text if not c.isdigit()])
    filtered_text = filtered_text.replace('-', ' ')
    filtered_text = ' '.join([lemmatizer.lemmatize(w) for w in filtered_text.split()])
    return filtered_text


def persist_model(clf, description):
    """ saves pickled classifier in /model_assets folder with naming convention: model_[description].pkl

    Parameters
    -------------
        clf: (obj) scikit-learn trained model
        description: (str) model version/descriptor
    """
    model_path = open(os.path.join(os.pardir, "model_assets/model_{}.pkl".format(description)), "wb")
    pickle.dump(clf, model_path)
    print('Model Saved.')


def build_encoder(text, count_vectorizer=None, tf_idf=None):
    """ builds a text feature extractor given an iterable of text data

    Parameters
    ---------------
        text: (list or series) of text data to transoform
        count_vectorizer: (bool) If `True` transforms into BoW model
        tf_idf: (bool) If `True` transforms into TF-IDF representation

    """

    if count_vectorizer:
        vectorizer = CountVectorizer()
        vectorizer.fit(text)
        return vectorizer

    if tf_idf:
        transformer = TfidfVectorizer()
        transformer.fit(text)
        return transformer


def persist_vectorizer(vectorizer, description):
    """ saves bag-of-words vectorizer in /model_assets folder with naming convention: vectorizer_[description].pkl

    Parameters
    -------------
        vectorizer: (obj) sklearn vectorizer object
        description: (str) vectorizer version/descriptor
    """
    vectorizer_path = open(os.path.join(os.pardir, "model_assets/vectorizer_{}.pkl".format(description)), "wb")
    pickle.dump(vectorizer, vectorizer_path)
    print('Vectorizer Saved.')


def sample_data(df, n):
    """ prints to console n random samples of data in the data frame (e.g online comment and label)

    Parameters
    -------------
        df: pandas DataFrame to be sampled
         n: number of samples to generate

    """
    for label in set(df.label):
        subset = df[df.label == label]
        rand_idxs = [random.randint(0, subset.shape[0]) for _ in range(n)]
        for idx in rand_idxs:
            print('Label: {}\nIndex: {}\t{}\n'.format(subset.iloc[idx]['label'], idx, subset.iloc[idx]['text']))