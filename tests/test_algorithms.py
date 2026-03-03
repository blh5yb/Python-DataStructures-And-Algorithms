import pytest
from src.algorithms_problems import *

class TestLIS:
    @pytest.mark.parametrize(
        'input, expected',
        [
            ([10, 22, 9, 33, 21, 50, 41, 60], 5),
            ([3, 10, 2, 1, 20], 3),
            ([50, 3, 10, 7, 40, 80], 4),
            ([3, 4, 5, 1, 2, 3, 4], 4)
        ]
    )
    def test_longest_increasing_seq_len(self, input, expected):
        actual = longest_increasing_subsequence_len(input)
        print(actual)
        assert actual == expected
