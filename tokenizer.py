class Tokenizer:

    def __init__(self, text: str) -> None:
        self.text = text
        self.bytes = [int(byte) for byte in self.text.encode("utf-8")]
    
    def _get_stats(self) -> dict:
        counts = dict()

        for pair in zip(self.bytes, self.bytes[1:]):
            if pair in counts.keys():
                counts[pair] += 1
            else:
                counts[pair] = 1

        return counts
    
    def _sort_stats(stats: dict) -> list:
        return sorted(
            (x for x in stats.items()),
            key=lambda x: x[1],
            reverse=True
        )
    
    def _merge(tokens: list, pair: tuple[int, int], new_id: int) -> list:
        """
        This function merges occurrences of the pair in the tokens 
        and replaces them with new_id
        """

        for start in range(len(tokens) - 1):
            if (tokens[start] == pair[0] and tokens[start+1] == pair[1]):
                tokens[start] = new_id
                tokens.pop(start+1)

        return tokens