
from codetalker import Grammar, Translator
from codetalker.tokens import STRING, ID, NUMBER, WHITE, NEWLINE, ReToken, re, CharToken, StringToken
from codetalker.special import star, plus, _or, binop
from codetalker.grammar import ParseError

## TOKENS

class OP(ReToken):
    rx = re.compile('\\*\\*|[-+*/%]')

class OP(StringToken):
    strings = ['**', '[', '-', '+', '*', '/', '%']
    num = 7

class SYMBOL(ReToken):
    rx = re.compile('[()]')

class SYMBOL(CharToken):
    chars = '()'
    num = 2

## RUlES

'''order of operations:

    && || ; not using
    +-
    */%
    **
    ()
'''

expression = binop(list('-+'), list('*/%'), ['**'], value=NUMBER, ops_token=OP, name='BinOp', paren=True)

grammar = Grammar(start=expression, tokens = [SYMBOL, OP], ignore = [WHITE, NEWLINE], ast_tokens=[NUMBER])

m = Translator(grammar)

ast = grammar.ast_classes

import operator
ops = {'**':operator.pow, '*':operator.mul, '/':operator.div, '%':operator.mod, '+':operator.add, '-':operator.sub}

@m.translates(ast.BinOp)
def binop(node):
    value = m.translate(node.left)
    for op, right in zip(node.ops, node.values):
        nv = m.translate(right)
        value = ops[op.value](value, nv)
    return value

@m.translates(NUMBER)
def number(node):
    return float(node.value)

evaluate = m.from_string

