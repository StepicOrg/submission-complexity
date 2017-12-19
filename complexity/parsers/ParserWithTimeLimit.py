import sys
from antlr4 import Parser, TokenStream, ParserRuleContext
from typing import TextIO

from antlr4.error.Errors import CancellationException


class ParserWithTimeLimit(Parser):
    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.stop = False

    def enterRule(self, localctx:ParserRuleContext , state:int , ruleIndex:int):
        if self.stop:
            raise CancellationException("The calculation is interrupted by the time limit")
        super(ParserWithTimeLimit, self).enterRule(localctx , state , ruleIndex)
