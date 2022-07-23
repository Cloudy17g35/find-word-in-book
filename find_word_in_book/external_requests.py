import requests
from fastapi import HTTPException


def get_request(url: str):
    try:
        response:requests.Response = requests.get(url)
        return response
    except Exception as e:
        print(e)
        message: str = "dependency error"
        raise HTTPException(status_code=424,
                            detail=message
                            )
        


def abort_if_response_not_ok(response:requests.Response):
    if not response.ok:
        message = f"invalid status code:{response.status_code} from external site"
        raise HTTPException(status_code=424,
                            detail=message
                            )


def get_book_text(url:str, encoding:str) -> str:
    response = get_request(url)
    abort_if_response_not_ok(response)
    response.encoding = encoding
    text:str = response.text
    return text
