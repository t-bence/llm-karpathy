def main() -> None:
    from tokenizer import Tokenizer
    tokenizer = Tokenizer("aaaabc")
    print(tokenizer.tokenize(1))


if __name__ == "__main__":
    main()