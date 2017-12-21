import sys
from antlr4 import Parser, TokenStream, ParserRuleContext
from typing import TextIO

from antlr4.error.Errors import CancellationException


class InterruptibleParser(Parser):
    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.stop = False

    def enterRule(self, localctx:ParserRuleContext , state:int , ruleIndex:int):
        if self.stop:
            raise CancellationException("Parsing is interrupted")
        super(InterruptibleParser, self).enterRule(localctx, state, ruleIndex)
