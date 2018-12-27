# Brainfuck Tools (python-bftools)
Brainfuck Utils for MISC

## Parser

```py
>>> from bftools import Parser
>>> code = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'
>>> Parser(code).exe()
'Hello World!\n'
```
