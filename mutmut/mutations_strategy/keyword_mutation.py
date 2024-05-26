from mutmut.mutations_strategy.mutation import Mutation

class KeywordMutation(Mutation):
    def mutate(self, value, context, **_):
        if len(context.stack) > 2 and context.stack[-2].type in ('comp_op', 'sync_comp_for') and value in ('in', 'is'):
            return

        if len(context.stack) > 1 and context.stack[-2].type == 'for_stmt':
            return

        return {
            # 'not': 'not not',
            'not': '',
            'is': 'is not',  # this will cause "is not not" sometimes, so there's a hack to fix that later
            'in': 'not in',
            'break': 'continue',
            'continue': 'break',
            'True': 'False',
            'False': 'True',
        }.get(value)

    def get_mutate_pointer(self):
        return dict(value=self.mutate)