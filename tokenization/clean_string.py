import string
import re
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords as STOPWORDS


def tokenize_sentence(sentence:str) -> str:
    sentence = sentence.lower()
    sentence = remove_punctuation(sentence)
    sentence = remove_multiple_spaces(sentence)
    sentence = sentence.strip()
    return sentence


def remove_punctuation(s:str):
    punctuation:str  = string.punctuation + '”“'
    return s.translate(str.maketrans('',  '', punctuation))


def remove_multiple_spaces(s:str):
    regex = "\s\s+"
    return re.sub(regex, " ", s)


