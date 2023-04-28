# exp_parser
An arithmetic expression parser in Python

# Idea desc
- So basically I had a programming language implementation that I was working on [click here](https://github.com/Moody0101-X/kasper) and now I realized that I need to study more about the topic of parsing expressions, so this repo is like an experiment so I can get how much hard or easy it actually is to parse expressions in python before integrating this concept into the language.

# Quick start
```console
$ git clone https://github.com/Moody0101-X/exp_parser
$ cd exp_parser\src
$ python main.py
```

# main goal
- the main goal of this parser is just for short parsing and evaluating arithmetic expressions such as `(x + 1) * (6 * 20)` or `1 + 2 * 2 - 20 * (-10)`..
- making a REPLE to give expressions and get answers from scratch, no libs and no plugin just python built-in functions and string manipulation.
- REPLE front-end:
```console
$ REPLE > (1 + 1)
ans: 2
$ REPLE > (1 + 1) * (2 * 2)
ans: 8
```

# What data structure I think I will use for this
- Stacks: for simple calculations

# Resources

- [Shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm#Detailed_examples)
- [Shunting yard algorithm 2](https://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/#:~:text=If%20the%20incoming%20symbol%20is,left%20parenthesis%20and%20discard%20it.)
- [Evaluating the postfix expression](https://www.boardinfinity.com/blog/postfix-expression/)

