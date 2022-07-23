import pytest
import find_word_in_book.tokenization as tokenization
import find_word_in_book.external_request as external_request
import find_word_in_book.controllers as controllers
import find_word_in_book.validators as validators
from typing import List, Dict
from pydantic import ValidationError
TEST_URL = 'http://www.gutenberg.org/files/2701/2701-0.txt'
ENCODING = 'utf-8'

class Tests:
    
    def test_if_resp_ok(self):
        resp = external_request.get_request(TEST_URL, ENCODING)
        expected_status_code = 200
        assert resp.status_code == expected_status_code
    
    def test_if_resp_ok(self):
        text:str= external_request.get_book_text(TEST_URL, ENCODING)
        assert isinstance(text, str)
    
    def test_change_encoding_in_response(self):
        resp = external_request.get_request(TEST_URL)
        assert resp.encoding == "ISO-8859-1"
        resp.encoding = ENCODING
        assert resp.encoding == ENCODING
    
    def test_splitlines(self):
        text: str = "The quick brown\n" \
                    "fox jumps over\n\r" \
                    "\r\nthe lazy dog\n\r"
        expected: List[str] = ['The quick brown', 'fox jumps over', '', '', 'the lazy dog', '']
        actual = text.splitlines()
        assert actual == expected
    
    def test_remove_punctuation(self):
        text: str = "The quick brown." \
                    "~!fox, jumps over?" \
                    ",the; ”lazy” dog"
        actual = tokenization.remove_punctuation(text)
        expected = "The quick brown" \
                    "fox jumps over" \
                    "the lazy dog"
        assert actual == expected
        
    def test_tokenize_sentence(self):
        text: str = "   The quick brown.  " \
                    "~!fOX, jumps    over?  " \
                    ",the; ”lazy” dog    "
        actual = tokenization.tokenize_sentence(text)
        expected = ['the', 'quick', 'brown', 'fox', 
                    'jumps', 'over', 'the', 'lazy', 'dog']
        assert actual == expected
    
    
    def test_validator_invalid_book(self):
        test_data:Dict[str, str] = {"book_name": "foo",
                                    "word": "hello"}
        with pytest.raises(Exception) as e:
            validators.GetBookAndWordRequest(**test_data)
        
        assert e.type == ValidationError
    
    def test_validator_invalid_word_length(self):
        test_data:Dict[str, str] = {"book_name": "idiot",
                            "word": "k"}
        with pytest.raises(Exception) as e:
            validators.GetBookAndWordRequest(**test_data)
    
        assert e.type == ValidationError

    def test_validator_word_in_stopwords(self):
        test_data:Dict[str, str] = {"book_name": "idiot",
                            "word": "i"}
        with pytest.raises(Exception) as e:
            validators.GetBookAndWordRequest(**test_data)
    
        assert e.type == ValidationError
    
