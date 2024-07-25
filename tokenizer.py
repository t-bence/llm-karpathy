class Tokenizer:

    def __init__(self, text: str) -> None:
        self.text = text
    
    def _get_stats(self) -> dict:
        bytes = [int(byte) for byte in self.text.encode("utf-8")]

        counts = dict()

        for pair in zip(bytes, bytes[1:]):
            if pair in counts.keys():
                counts[pair] += 1
            else:
                counts[pair] = 1

        return counts