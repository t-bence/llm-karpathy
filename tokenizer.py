class Tokenizer:

    def __init__(self, text: str) -> None:
        self.text = text
        self.bytes = [int(byte) for byte in self.text.encode("utf-8")]
        self.merges = None
    
    @staticmethod
    def _get_stats(tokens: list) -> dict:
        counts = dict()

        for pair in zip(tokens, tokens[1:]):
            if pair in counts.keys():
                counts[pair] += 1
            else:
                counts[pair] = 1

        return counts
    
    @staticmethod
    def _get_sorted_stats(tokens: list) -> list:
        stats = Tokenizer._get_stats(tokens)
        return sorted(
            (x for x in stats.items()),
            key=lambda x: x[1],
            reverse=True
        )
    
    @staticmethod
    def _merge(tokens: list, pair: tuple[int, int], new_id: int) -> list:
        """
        This function merges occurrences of the pair in the tokens 
        and replaces them with new_id
        """
        result = []
        i = 0
        while i < len(tokens):
            if (i < len(tokens)-1 and tokens[i] == pair[0] and tokens[i+1] == pair[1]):
                result.append(new_id)
                i+=2
            else:
                result.append(tokens[i])
                i+=1

        return result
    
    def tokenize(self, num_merges: int) -> list:
        tokens = self.bytes.copy()
        self.merges = dict()

        for i in range(num_merges):
            new_id = 256 + i
            stats = Tokenizer._get_sorted_stats(tokens)

            pair = stats[i][0] # gets the most common byte pair
            tokens = Tokenizer._merge(tokens, pair, new_id)
            self.merges[pair] = new_id

        return tokens
    

    def decode(self, ids: list[int]) -> str:
        """Return a string from a list of token integers"""
        if self.merges is None:
            raise ValueError("First call tokenize()!")
        
        # create a dict that is new_id -> pair with new_id in decreasing order
        conversion = list()
        for pair, value in self.merges.items():
            conversion.append((value, pair[0], pair[1]))

        for new_id, old0, old1 in sorted(conversion, key=lambda x: x[0], reverse=True):
            for index, byte in enumerate(ids):
                if byte == new_id:
                    ids[index] = old0
                    ids.insert(index+1, old1)

        return bytes(ids).decode("utf-8")
    