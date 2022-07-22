import find_word_in_book.tokenization as tokenization
from typing import List


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