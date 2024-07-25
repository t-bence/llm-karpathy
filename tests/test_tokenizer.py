from tokenizer import Tokenizer

char_for_a = 97

def test_unity():
    assert 1 == 1

def test_Tokenizer():
    x = Tokenizer("")
    assert x is not None

def test_stats():
    text = "aaaabc"
    result = Tokenizer(text)._get_stats()
    assert result[(char_for_a, char_for_a)] == 3