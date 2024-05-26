from mutmut.mutations_strategy.mutation import Mutation
class DecoratorMutation(Mutation):
    def mutate(self, children, **_):
        assert children[-1].type == 'newline'
        return children[-1:]

    def get_mutate_pointer(self):
        return dict(children=self.mutate)