from pydantic import BaseModel, validator
import find_word_in_book.book_mapper as book_mapper
from typing import List
from nltk.corpus import stopwords as STOPWORDS


class GetBookAndWordRequest(BaseModel):
    book_name: str
    word: str

    @validator('book_name')
    def book_name_must_be_valid(cls, book_name):
        possible_books: List[str] = list(book_mapper.get_possible_books().keys())
        
        if book_name.lower().strip() not in possible_books:
            message: str = f'{book_name} is not in possible_books: '\
                           f"{', '.join(possible_books)}"
            raise ValueError(message)
        return book_name.lower().strip()


    @validator('word')
    def validate_word(cls, word):
        stopwords = STOPWORDS.words('english')
        message:str = f"word length must be greater or equal than 2 " \
                      f"and word cannot be a stopword,"\
                      f"list of stopwords: {', '.join(stopwords)}"
        if len(word) < 2 or word.lower() in stopwords:
            raise ValueError(message)
        return word.lower().strip()
