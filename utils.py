from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string


def clean_text(text):
    """ Cleans the input text from prediction endpoint.


    :param text: (str) text to clean
    :return: (str) post-processed clean text
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