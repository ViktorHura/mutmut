from mutmut.mutations_strategy.mutation import Mutation
from parso.python.tree import Keyword
class AndOrTestMutation(Mutation):
    def mutate(self, children, node, **_):
        children = children[:]
        children[1] = Keyword(
            value={'and': ' or', 'or': ' and'}[children[1].value],
            start_pos=node.start_pos,
        )
        return children

    def get_mutate_pointer(self):
        return dict(children=self.mutate)