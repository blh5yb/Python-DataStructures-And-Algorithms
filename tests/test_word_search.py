import pytest
from src.tree_word_search import *


class TestNode:
    def test_new_word_insert(self):
        """test inserting new word is added"""
        root = Node()
        for w in ["Stop", "Wont", "Word", "Stop"]:
            root.insert(w)

        branch = root.children['w'].children['o'].children['r'].children['d']
        assert branch.is_end == True
        assert len(root.children.items()) == 2
        assert root.children["w"].num_entries == 2
        assert root.children["s"].num_entries == 2


class TestWordSearch:
    @pytest.mark.parametrize(
        'new_word, current_set, expected',
        [
            ("Stop", set(), True),
            ("Stop", {"Stop"}, False),
        ]
    )
    def test_add_new_word(self, new_word, current_set, expected):
        lexicon = WordSearch()
        lexicon.lexicon_set = current_set
        result = lexicon.add_word(new_word)

        assert result == expected

    @pytest.mark.parametrize(
        'my_word, current_words, expected',
        [
            ("Word", {"word", "stop"}, True),
            ("notWord", {"stop"}, False),
        ]
    )
    def test_is_word(self, my_word, current_words, expected):
        lexicon = WordSearch()
        lexicon.lexicon_set = current_words
        result = lexicon.is_word(my_word)
        assert result == expected

    @pytest.mark.parametrize(
        'my_prefix, expected',
        [
            ("Wo", True),
            ("Sto", True),
            ("Stor", False),
            ("No", False),
        ]
    )
    def test_is_prefix(self, my_prefix, expected):
        lexicon = WordSearch()
        # lexicon.lexicon_set = {"word", "stop", "wont"}
        for word in {"word", "stop", "wont", "wor"}:
            lexicon.add_word(word)

        result = lexicon.is_prefix(my_prefix)
        assert result == expected

    @pytest.mark.parametrize(
        'my_prefix, expected',
        [
            ("Wo", ["word", "wont"]),
            ("Sto", ["stop"]),
            ("Wor", ["word"]),
            ("No", []),
        ]
    )
    def test_get_words(self, my_prefix, expected):
        lexicon = WordSearch()
        for word in {"word", "stop", "wont"}:
            lexicon.add_word(word)

        result = lexicon.get_words(my_prefix)
        assert set(result) == set(expected)

    @pytest.mark.parametrize(
        'my_prefix, expected',
        [
            ("WO", 2),
            ("Sto", 1),
            ("Wor", 1),
            ("No", 0),
        ]
    )
    def test_get_prefix_counts(self, my_prefix, expected):
        lexicon = WordSearch()
        for word in {"word", "stop", "wont"}:
            lexicon.add_word(word)

        result = lexicon.get_prefix_counts(my_prefix)
        assert result == expected