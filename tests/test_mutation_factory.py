from mutmut import mutations_strategy


def test_correct_strategy_factory_getter():
    correct_mutations = {
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

    # Loop through the mutations_to_test dictionary
    for strategy_name, mutation_instance in correct_mutations.items():
        # Correct class type
        expected_class = type(mutations_strategy.StrategyFactory.get_strategy(strategy_name))
        # Check if correct
        assert type(mutation_instance) == expected_class




