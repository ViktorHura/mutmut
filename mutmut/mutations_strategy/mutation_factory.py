from mutmut import mutations_strategy


class StrategyFactory:
    @staticmethod
    def get_mutations_dict():
        return {
            'operator': mutations_strategy.OperatorMutation(),
            'keyword': mutations_strategy.KeywordMutation(),
            'number': mutations_strategy.NumberMutation(),
            'name': mutations_strategy.NameMutation(),
            'string': mutations_strategy.StringMutation(),
            'fstring': mutations_strategy.FStringMutation(),
            'argument': mutations_strategy.ArgumentMutation(),
            'or_test': mutations_strategy.AndOrTestMutation(),
            'and_test': mutations_strategy.AndOrTestMutation(),
            'lambdef': mutations_strategy.LambdaMutation(),
            'expr_stmt': mutations_strategy.ExpressionMutation(),
            'decorator': mutations_strategy.DecoratorMutation(),
            'annassign': mutations_strategy.ExpressionMutation(),
            # TODO: detect regexes and mutate them in nasty ways? Maybe mutate all strings as if they are regexes
        }
    @staticmethod
    def get_strategy(strategy_type):
        strategies = StrategyFactory.get_mutations_dict()
        return strategies.get(strategy_type, None) # returns None if key not present
