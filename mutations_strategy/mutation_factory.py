import mutations_strategy
class StrategyFactory:
    @staticmethod
    def get_strategy(strategy_type):
        strategies = {
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
        }

        return strategies.get(strategy_type, None) # returns None if key not present
