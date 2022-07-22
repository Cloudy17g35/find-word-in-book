import main
import find_word_in_book.tokenization as tokenization
from typing import List


class Tests:
    def test_if_resp_ok(self):
        resp = main.get_request(main.BOOK_URL)
        expected_status_code = 200
        assert resp.status_code == expected_status_code
    
    def test_change_encoding_in_response(self):
        resp = main.get_request(main.BOOK_URL)
        assert resp.encoding == "ISO-8859-1"
        resp.encoding = main.ENCODING
        assert resp.encoding == main.ENCODING
        
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
        
    def test_remove_punctuation(self):
        text: str = "   The quick brown.  " \
                    "~!fOX, jumps over?  " \
                    ",the; ”lazy” dog    "
        actual = tokenization.tokenize_sentence(text)
        expected = "The quick brown" \
                    "fox jumps over" \
                    "the lazy dog"
        assert actual == expected
    

        