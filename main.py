BOOK_URL = 'https://www.gutenberg.org/files/2701/2701-0.txt'
ENCODING = 'utf-8'
WORD = 'money'
import requests
from typing import List
import string_operations.splitter, string_operations.clean_string


def get_request(url: str):
    response:requests.Response = requests.get(url)
    return response


def abort_if_response_not_ok(response:requests.Response):

    if not response.ok:
        raise ValueError("invalid response")


def get_clean_sentences(splited:List[str]) -> List[str]:
    res = []
    for sentence in splited:
        if not sentence:
            continue
        sentence = string_operations.clean_string.clean_sentence(sentence)
        res.append(sentence)
    return res


def count_word_occurences_in_sentence(sentence:str, word:str) -> int:
    return sentence.split().count(word)


def check_if_word_in_sentence(sentence:str, word:str) -> bool:
    return word in set(sentence.split())


def get_word_count_and_lines(sentences:List[str]):
    word_count = 0
    lines_where_word_occured = []
    for sentence in sentences:
        cur_count = count_word_occurences_in_sentence(sentence, WORD)
        word_count += cur_count
        if check_if_word_in_sentence(sentence, WORD):
            lines_where_word_occured.append(sentence)
    return word_count, lines_where_word_occured

api_response = {
    'occurences': None,
    'lines': []
                }


def main():
    response = get_request(BOOK_URL)
    abort_if_response_not_ok(response)
    response.encoding = ENCODING
    text:str = response.text
    text_splited:List[str] = string_operations.splitter.split_lines(text)
    cleaned_sentences = get_clean_sentences(text_splited)
    word_count, lines_where_word_occured = get_word_count_and_lines(cleaned_sentences)
    api_response["occurences"] = word_count
    api_response["lines"] = lines_where_word_occured
    print(len(lines_where_word_occured))
    print(api_response)
        


if __name__ == "__main__":
    main()
    