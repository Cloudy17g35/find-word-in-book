from typing import List, Dict


def get_api_response(occurences:int, lines:List[str]):

    api_response:Dict[str, str] = {
        'occurences': occurences,
        'lines': lines
        }
    
    return api_response