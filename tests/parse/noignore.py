#!/usr/bin/env python

from codetalker import Grammar
from codetalker.tokens import INT, WHITE, CharToken, ID, STRING, SSTRING
from codetalker.special import star, plus, _or, no_ignore
from codetalker.errors import ParseError

class SYMBOL(CharToken):
    chars = '@'

def at(rule):
    rule | (no_ignore('@', ID), _or(STRING, SSTRING))

g = Grammar(start=at, tokens=[SYMBOL, ID, STRING, SSTRING, WHITE], ignore=[WHITE])

from codetalker import testing

parse_rule = testing.parse_rule(__name__, g)

parse_rule(at, (
    ' @one"teo"',
    '@one"two"',
    '@one "two"',
    '@some          \'one\'',
    ), (
    '@ one "two"',
    ))

if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            print 'testing', name
            fn()
            print 'test passed'
    print 'Finished!'



# vim: et sw=4 sts=4
