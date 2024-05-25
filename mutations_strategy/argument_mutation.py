from mutations_strategy.mutation import Mutation
from parso.python.tree import Name
class ArgumentMutation(Mutation):
    def mutate(self, children, context, **_):
        """Mutate the arguments one by one from dict(a=b) to dict(aXXX=b).

        This is similar to the mutation of dict literals in the form {'a': b}.

        :type context: Context
        """
        if len(context.stack) >= 3 and context.stack[-3].type in ('power', 'atom_expr'):
            stack_pos_of_power_node = -3
        elif len(context.stack) >= 4 and context.stack[-4].type in ('power', 'atom_expr'):
            stack_pos_of_power_node = -4
        else:
            return

        power_node = context.stack[stack_pos_of_power_node]

        if power_node.children[0].type == 'name' and power_node.children[0].value in context.dict_synonyms:
            c = children[0]
            if c.type == 'name':
                children = children[:]
                children[0] = Name(c.value + 'XX', start_pos=c.start_pos, prefix=c.prefix)
                return children
