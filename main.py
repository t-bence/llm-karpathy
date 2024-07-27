def main() -> None:
    from tokenizer import Tokenizer
    tokenizer = Tokenizer("aaaabc")
    print(tokenizer.tokenize(1))
    print(tokenizer.decode([256, 256, 98, 99]))


if __name__ == "__main__":
    main()