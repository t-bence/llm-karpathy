from tokenizer import Tokenizer

CHAR_A = 97
CHAR_B = 98
CHAR_C = 99

def test_unity():
    assert 1 == 1

def test_Tokenizer():
    x = Tokenizer("")
    assert x is not None

def test_stats():
    text = "aaaabc"
    result = Tokenizer(text)._get_stats()
    correct = {
        (CHAR_A, CHAR_A): 3,
        (CHAR_A, CHAR_B): 1,
        (CHAR_B, CHAR_C): 1
    }
    assert result == correct

def test_sort():
    text = "aaaabc"
    result = Tokenizer._sort_stats(Tokenizer(text)._get_stats())
    assert result[0][0] == (CHAR_A, CHAR_A)
    assert result[0][1] == 3

def test_merge():
    result = Tokenizer._merge([CHAR_A, CHAR_A, CHAR_B, CHAR_C], (CHAR_A, CHAR_A), 256)
    assert result == [256, CHAR_B, CHAR_C]

def test_merge_karpathy_example():
    # This is the example in the video lecture
    input = [5, 6, 6, 7, 9, 1]
    result = Tokenizer._merge(input, (6, 7), 99)
    assert input == [5, 6, 99, 9, 1]