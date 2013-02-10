from tokens import Token
import types
import inspect
import copy
from nodes import AstNode

from errors import CodeTalkerException

class UnhandledTokenException(CodeTalkerException):
    """ Raised by Translator when no function is registered to handle a token
    """
    def __init__(self, tree):
        Error.__init__(self,
                "no rule to translate %s" % tree.__class__.__name__)

class Translator:
    def __init__(self, grammar):
        self._grammar = grammar
        self._register = {Token: lambda tree : tree.value}

    def translates(self, what):
        def meta(func):
            self._register[what] = func
            return func
        return meta

    def translate(self, tree, *args, **kwargs):
        if tree is None:
            return None

        if tree.__class__ not in self._register:
            raise TranslatorException()

        if "scope" in kwargs:
            return self._register[tree.__class__](kwargs["scope"], tree,
                                                  *args, **kwargs)
        else:
            return self._register[tree.__class__](tree, *args, **kwargs)

    def from_string(self, text, *args, **kwargs):
        tree = self._grammar.get_ast(text)
        return self.translate(tree, *args, **kwargs)
