BOOK_URL = 'https://www.gutenberg.org/files/2701/2701-0.txt'
import requests
from typing import List


def get_request(url: str):
    response:requests.Response = requests.get(url)
    return response

def abort_if_response_not_ok(response:requests.Response):
    if not response.ok:
        raise ValueError("invalid response")

def decode_response(response: requests.Response,
                    encoding:str="utf8"):
    return response.content.decode(encoding=encoding)

def main():
    response = get_request(BOOK_URL)
    abort_if_response_not_ok(response)
    text:str = decode_response(response)
    text_splited:List[str] = text.splitlines()
    print(text_splited)

    
if __name__ == "__main__":
    main()
    