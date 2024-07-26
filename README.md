# llm-karpathy
Learn about LLMs following Andrej Karpathy's videos

Video about tokenization: https://www.youtube.com/watch?v=zduSFxRajkE

## How to run
`python main.py`

## How to run tests
`python -m pytest`

## Questions
- What will happen to overlapping tokens? E.g. aaaabc, there are 3 aa tokens there but I will only merge two in the first go.
- What if the text is not long enough?