
from codetalker import Grammar
from codetalker.tokens import STRING, ID, NUMBER, WHITE, NEWLINE, INDENT, DEDENT, ReToken, re
from codetalker.special import star, plus, _or
from codetalker.grammar import ParseError

def start(rule):
    rule | (SMALL, NEWLINE, INDENT, SMALL, [NEWLINE, DEDENT, SMALL])

class SMALL(ReToken):
    rx = re.compile('hello')

grammar = Grammar(start=start, tokens=[SMALL, WHITE, NEWLINE], indent=True, ignore=[WHITE])

def test_indent():
    tree = grammar.process('hello\n  hello')

def test_dedent():
    tree = grammar.process('hello\n hello\nhello')

if __name__ == '__main__':
    for name, fn in globals().items():
        if name.startswith('test_'):
            print 'testing', fn
            fn()
            print 'test passed'
    print 'Finished!'

