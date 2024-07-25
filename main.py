def main() -> None:
    from tokenizer import Tokenizer
    tokenizer = Tokenizer("aaaabc")
    print(tokenizer._get_stats())


if __name__ == "__main__":
    main()