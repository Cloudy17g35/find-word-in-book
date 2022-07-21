import pytest
import main

class Tests():
    def test_if_resp_ok(self):
        resp = main.get_request(main.BOOK_URL)
        expected_status_code = 200
        assert resp.status_code == expected_status_code
    
    def test_if_response_text_is_string(self):
        resp = main.get_request(main.BOOK_URL)
        text:str = main.decode_response(resp)
        assert type(text) == str
        