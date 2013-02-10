
from codetalker import Grammar
from codetalker.tokens import *
from codetalker.special import *

def start(rule):
    rule | plus(value)

def value(rule):
    rule | ([ID], STRING)

g = Grammar(start=start, tokens=[ID, STRING, WHITE], ignore=[WHITE])

def test_one():
    tree = g.get_ast('"string" "string" "strin" ')
    assert len(tree) == 3

def test_onother():
    st = '"string" "string" "strin" '
    tree = g.process(st)
    assert str(tree) == st

def test_two():
    tree = g.get_ast('one "two" three "four" five "six"')
    assert len(tree) == 3

def test_three():
    tree = g.get_ast('"one" two "three" "four" five "six"')
    assert len(tree) == 4


