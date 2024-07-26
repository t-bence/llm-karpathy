def main() -> None:
    from tokenizer import Tokenizer
    tokenizer = Tokenizer("aaaabc")
    stats = tokenizer._get_stats()
    print(Tokenizer._sort_stats(stats))
    #print(tokenizer._merge(1))


if __name__ == "__main__":
    main()