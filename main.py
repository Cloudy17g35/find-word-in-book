BOOK_URL = 'https://www.gutenberg.org/files/2701/2701-0.txt'
ENCODING = 'utf-8'
WORD = 'mouse'
from typing import List, Dict
import find_word_in_book.controllers as controllers
import find_word_in_book.external_request as external_request
import find_word_in_book.api_response as api_response


def main():
    text:str = external_request.get_book_text(BOOK_URL, ENCODING)
    all_lines:List[str] = text.splitlines()
    word_count, lines_where_word_occured = controllers.get_word_count_and_lines_where_word_occured(all_lines, WORD)
    response:Dict[str, str] = api_response.get_api_response(word_count, lines_where_word_occured)
    print(response)


if __name__ == "__main__":
    main()
    