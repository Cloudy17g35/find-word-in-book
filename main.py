BOOK_URL = 'https://www.gutenberg.org/files/2701/2701-0.txt'
ENCODING = 'utf-8'
import requests
from typing import List
import string_operations.splitter, string_operations.clean_string



def get_request(url: str):
    response:requests.Response = requests.get(url)
    return response

def abort_if_response_not_ok(response:requests.Response):
    if not response.ok:
        raise ValueError("invalid response")

def set_encoding_in_response(response: requests.Response,
                             encoding=ENCODING) -> requests.Response:
    pass
    


def get_text_from_response(response:requests.Response) -> str:
    return response.text


def clean_sentence(sentence):
    sentence = string_operations.clean_string.remove_punctuation(sentence)
    sentence = string_operations.clean_string.remove_white_spaces(sentence)
    sentence = sentence.strip()
    sentence = sentence.lower()
    sentence = string_operations.clean_string.remove_stopwords(sentence)
    return sentence


def get_clean_sentences(splited) -> List[str]:
    res = []
    for sentence in splited:
        if not sentence:
            continue
        sentence = clean_sentence(sentence)
        res.append(sentence)
    return res


def main():
    response = get_request(BOOK_URL)
    abort_if_response_not_ok(response)
    response.encoding = ENCODING
    text:str = response.text
    text_splited:List[str] = string_operations.splitter.split_lines(text)
    cleaned_sentences = get_clean_sentences(text_splited)
    print(cleaned_sentences)
    
if __name__ == "__main__":
    main()
    