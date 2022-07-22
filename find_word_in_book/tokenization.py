import string
from typing import List


def tokenize_sentence(sentence:str) -> List[str]:
    sentence = sentence.lower()
    sentence = remove_punctuation(sentence)
    sentence = sentence.strip()
    return sentence.split()


def remove_punctuation(s:str):
    punctuation:str  = string.punctuation + '”“'
    return s.translate(str.maketrans('',  '', punctuation))


def count_word_occurences_in_tokenized_sentence(tokenized_sentence:List[str], 
                                                word:str) -> int:
    return tokenized_sentence.count(word)


def check_if_word_in_tokenized_sentence(tokenized_sentence:List[str], 
                                        word:str) -> bool:
    return word in set(tokenized_sentence)
