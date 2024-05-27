from mutmut.mutations_strategy.mutation import Mutation
import utils
array_subscript_pattern = utils.ASTPattern("""
_name[_any]
#       ^
""")


function_call_pattern = utils.ASTPattern("""
_name(_any)
#       ^
""")
class NameMutation(Mutation):
    def __init__(self):
        self.array_subscript_pattern = utils.ASTPattern(""" # no tabs, or test_mutation.py will fail
_name[_any]
#       ^
""")

        self.function_call_pattern = utils.ASTPattern("""
_name(_any)
#       ^
""")

    def mutate(self, node, value, **_):
        """"
        Mutates names defined in dict simple_mutants
        """
        simple_mutants = {
            'True': 'False',
            'False': 'True',
            'deepcopy': 'copy',
            'None': '""',
            # TODO: probably need to add a lot of things here... some builtins maybe, what more?
        }
        if value in simple_mutants:
            return simple_mutants[value]

        if self.array_subscript_pattern.matches(node=node):
            return 'None'

        if self.function_call_pattern.matches(node=node):
            return 'None'

    def get_mutate_pointer(self):
        return dict(value=self.mutate)