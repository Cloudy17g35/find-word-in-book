BOOK_URL = 'https://www.gutenberg.org/files/2701/2701-0.txt'
ENCODING = 'utf-8'
WORD = 'doctor'
import requests
from typing import List
import tokenization.splitter, tokenization.clean_string


def get_request(url: str):
    response:requests.Response = requests.get(url)
    return response


def abort_if_response_not_ok(response:requests.Response):

    if not response.ok:
        raise ValueError("invalid response")



def count_word_occurences_in_sentence(sentence:str, word:str) -> int:
    return sentence.split().count(word)


def check_if_word_in_sentence(sentence:str, word:str) -> bool:
    return word in set(sentence.split())


api_response = {
    'occurences': None,
    'lines': []
                }


def main():
    response = get_request(BOOK_URL)
    abort_if_response_not_ok(response)
    response.encoding = ENCODING
    
    text:str = response.text
    
    all_lines:List[str] = tokenization.splitter.split_lines(text)
    word_count:int = 0
    lines_where_word_occured:List[str] = []
    
    for sentence in all_lines:
        if not sentence:
            continue
        tokenized_sentence:str = tokenization.clean_string.tokenize_sentence(sentence)
        cur_count:int = count_word_occurences_in_sentence(tokenized_sentence, WORD)
        word_count += cur_count
        if check_if_word_in_sentence(tokenized_sentence, WORD):
            lines_where_word_occured.append(sentence)
        
    api_response["occurences"] = word_count
    api_response["lines"] = lines_where_word_occured
    print(api_response)


if __name__ == "__main__":
    main()
    