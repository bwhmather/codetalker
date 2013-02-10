
from codetalker import Grammar
from codetalker.tokens import INT, WHITE, CharToken, ID, STRING, SSTRING
from codetalker.special import star, plus, _or, no_ignore, _not
from codetalker.errors import ParseError

class SYMBOL(CharToken):
    chars = '@;}'

def at(rule):
    rule | (no_ignore('@', ID), _or(STRING, SSTRING, star(_not(_or(';','}')))), ';')
    rule | star(_not(_or(';','}')))

g = Grammar(start=at, tokens=[SYMBOL, ID, STRING, SSTRING, WHITE], ignore=[WHITE])

from codetalker import testing

parse_rule = testing.parse_rule(__name__, g)

parse_rule(at, (
    '@one "hi";',
    '@two "ho" ;',
    '@three lots of stuff;',
    '@four many" m"ore;',
    'random junk',
    '@I know you can',
    '@do "it" yes',
    ))

if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            print 'testing', name
            fn()
            print 'test passed'
    print 'Finished!'

