BOOK_URL = 'https://www.gutenberg.org/files/2701/2701-0.txt'
ENCODING = 'utf-8'
WORD = 'mouse'
from typing import List
import find_word_in_book.tokenization as tokenization
import find_word_in_book.external_request as external_request


def get_word_count_and_lines_where_word_occured(lines:List[str], 
                                                word:str):
        
        word_count:int = 0
        lines_where_word_occured:List[str] = []
        
        for sentence in lines:
            if not sentence:
                continue
            tokenized_sentence:str = tokenization.tokenize_sentence(sentence)
            cur_count:int = tokenization.count_word_occurences_in_tokenized_sentence(tokenized_sentence, word)
            word_count += cur_count
            if tokenization.check_if_word_in_tokenized_sentence(tokenized_sentence, word):
                lines_where_word_occured.append(sentence)
        return word_count, lines_where_word_occured



api_response = {
    'occurences': None,
    'lines': []
                }


def main():
    text:str = external_request.get_book_text(BOOK_URL, ENCODING)
    all_lines:List[str] = text.splitlines()
    word_count, lines_where_word_occured = get_word_count_and_lines_where_word_occured(all_lines, WORD)
    api_response["occurences"] = word_count
    api_response["lines"] = lines_where_word_occured
    

if __name__ == "__main__":
    main()
    