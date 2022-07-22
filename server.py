import find_word_in_book.controllers as controllers
from fastapi import FastAPI


app:FastAPI = FastAPI()

@app.get('/books/')
async def get_word_and_lines_endpoint(word:str, 
                                      book_name:str):
    return controllers.get_word_count_and_lines_where_word_occured(word, 
                                                                   book_name)
