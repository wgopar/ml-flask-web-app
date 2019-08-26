from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pickle
import string
import random
import os


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


def persist_vectorizer(vectorizer, description):
    """ saves bag-of-words vectorizer in /model_assets folder with naming convention: vectorizer_[description].pkl

    Attributes
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