class Tokenizer:

    def __init__(self, text: str) -> None:
        self.text = text
        self.bytes = [int(byte) for byte in self.text.encode("utf-8")]
    
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
    def _sort_stats(stats: dict) -> list:
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

        for i in range(num_merges):
            new_id = 256 + i
            stats = Tokenizer._sort_stats(
                Tokenizer._get_stats(tokens)
            )
            pair = stats[i][0] # gets the most common byte pair
            tokens = Tokenizer._merge(tokens, pair, new_id)

        return tokens