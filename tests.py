import server
import find_word_in_book.tokenization as tokenization
import find_word_in_book.external_request as external_request
import find_word_in_book.controllers as controllers
from typing import List


class Tests:
    
    def test_if_resp_ok(self):
        resp = external_request.get_request(server.BOOK_URL)
        expected_status_code = 200
        assert resp.status_code == expected_status_code
    
    def test_if_resp_ok(self):
        text:str= external_request.get_book_text(server.BOOK_URL, server.ENCODING)
        assert isinstance(text, str)
    
    def test_change_encoding_in_response(self):
        resp = external_request.get_request(server.BOOK_URL)
        assert resp.encoding == "ISO-8859-1"
        resp.encoding = server.ENCODING
        assert resp.encoding == server.ENCODING
    
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
    
    def test_get_get_word_count_and_lines_where_word_occured(self):
        lines: str = ['the quick brown',
                    'fox jumps over',
                    'the lazy dog']
        
        word: str = 'the'
        word_count, lines_where_word_occured = controllers.get_word_count_and_lines_where_word_occured(lines, word)
        expected_word_count, expected_lines_where_word_occured = 2, ['the quick brown', 'the lazy dog']
        assert (word_count, lines_where_word_occured) == (expected_word_count , expected_lines_where_word_occured)

        