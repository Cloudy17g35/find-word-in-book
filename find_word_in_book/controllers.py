import find_word_in_book.tokenization as tokenization
import find_word_in_book.external_request as external_request
import find_word_in_book.responses as responses
import find_word_in_book.book_mapper as book_mapper
import find_word_in_book.validators as validators
from pydantic import ValidationError
from fastapi import HTTPException
from typing import List, Dict
ENCODING = 'utf-8'



def get_word_count_and_lines_where_word_occured(
    book_name:str,
    word:str):
    try:
        user_request = validators.GetBookAndWordRequest(
            book_name=book_name,
            word=word)
    except ValidationError as e:
        raise HTTPException(status_code=400, 
                            detail=e.errors())
    url:str = book_mapper.map_book_name_to_url(user_request.book_name)
    text:str = external_request.get_book_text(url, ENCODING)
    all_sentences: List[str] = text.splitlines()
    word_count:int = 0
    lines_where_word_occured: List[str] = []
    
    for sentence in all_sentences:
        if not sentence:
            continue
        tokenized_sentence:str = tokenization.tokenize_sentence(sentence)
        cur_count:int = tokenization.count_word_occurences_in_tokenized_sentence(tokenized_sentence, word)
        word_count += cur_count
        if tokenization.check_if_word_in_tokenized_sentence(tokenized_sentence, word):
            lines_where_word_occured.append(sentence)
    response:Dict[str, str] = responses.valid_response(word_count, lines_where_word_occured)
    return response
        