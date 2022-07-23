import find_word_in_book.controllers as controllers
from fastapi import FastAPI

app:FastAPI = FastAPI()

@app.get('/books/')
async def get_word_and_lines_endpoint(book_name:str,
                                      word:str):
    
    return controllers.get_word_count_and_lines_where_word_occured(book_name, 
                                                                   word)
