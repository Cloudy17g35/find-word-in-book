import string
import re
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords as STOPWORDS


def remove_punctuation(s:str):
    punctuation:str  = string.punctuation + '”“'
    return s.translate(str.maketrans('',  '', punctuation))


def remove_multiple_spaces(s:str):
    regex = "\s\s+"
    return re.sub(regex, " ", s)


def remove_stopwords(s:str):
    stopwords = STOPWORDS.words('english')
    return " ".join([word for word in s.split() if word not in (stopwords)])


