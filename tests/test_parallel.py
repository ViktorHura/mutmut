from mutmut.__main__ import parallel_test_subset

def test_parallel_test_subset():
    mut_by_file = {
        'a': [0, 1 ,2, 3],
        'b': [4, 5, 6, 7, 8],
        'c': [9, 10],
        'd': [11, 12, 13]
    }

    subset = parallel_test_subset(1, 5, mut_by_file)
    expected = {'a': [0, 1]}
    assert subset == expected

    subset = parallel_test_subset(2, 5, mut_by_file)
    expected = {'a': [2, 3]}
    assert subset == expected

    subset = parallel_test_subset(3, 5, mut_by_file)
    expected = {'b': [4, 5]}
    assert subset == expected

    subset = parallel_test_subset(4, 5, mut_by_file)
    expected = {'b': [6, 7]}
    assert subset == expected

    subset = parallel_test_subset(5, 5, mut_by_file)
    expected = {'b': [8], 'c': [9, 10], 'd': [11, 12, 13]}
    assert subset == expected

    subset = parallel_test_subset(1, 2, mut_by_file)
    expected = {'a': [0, 1, 2, 3], 'b': [4, 5, 6]}
    assert subset == expected

    subset = parallel_test_subset(2, 2, mut_by_file)
    expected = {'b': [7, 8], 'c': [9, 10], 'd': [11, 12, 13]}
    assert subset == expected

