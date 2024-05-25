from mutations_strategy.mutation import Mutation
from utils import *

class OperatorMutation(Mutation):
    def __init__(self):
        self.import_from_star_pattern = ASTPattern("""
from _name import *
#                 ^
""")
    def mutate(self, value, node, **_):
        if self.import_from_star_pattern.matches(node=node):
            return

        if value in ('*', '**') and node.parent.type == 'param':
            return

        if value == '*' and node.parent.type == 'parameters':
            return

        if value in ('*', '**') and node.parent.type in ('argument', 'arglist'):
            return

        return {
            '+': '-',
            '-': '+',
            '*': '/',
            '/': '*',
            '//': '/',
            '%': '/',
            '<<': '>>',
            '>>': '<<',
            '&': '|',
            '|': '&',
            '^': '&',
            '**': '*',
            '~': '',

            '+=': ['-=', '='],
            '-=': ['+=', '='],
            '*=': ['/=', '='],
            '/=': ['*=', '='],
            '//=': ['/=', '='],
            '%=': ['/=', '='],
            '<<=': ['>>=', '='],
            '>>=': ['<<=', '='],
            '&=': ['|=', '='],
            '|=': ['&=', '='],
            '^=': ['&=', '='],
            '**=': ['*=', '='],
            '~=': '=',

            '<': '<=',
            '<=': '<',
            '>': '>=',
            '>=': '>',
            '==': '!=',
            '!=': '==',
            '<>': '==',
        }.get(value)

    def get_mutate_pointer(self):
        return dict(value=self.mutate)