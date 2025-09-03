########################################################################################################################
# Tree & Hash Map Word searching
# Author: Barry Hykes Jr, bhykes@gmail.com
# version 1.0.0
########################################################################################################################


class Node:
    __slots__ = ['children', 'is_end', 'num_entries']
    def __init__(self):
        self.children = {} # new node
        self.is_end = False # to track words the match the pattern
        self.num_entries = 0 # How many matching prefixes
        return

    def insert(self, key):
        """
        Insert a word into the tree
        :param key: string/ substring to insert, str
        """
        first_char = key[0].lower()
        # check if char exists
        # create new branch for first_char
        if not self.children.get(first_char):
            self.children[first_char] = Node()

        # get the current node for first char
        child = self.children[first_char]
        child.num_entries += 1

        # recursively insert til reach the end of word
        if len(key) > 1:
            child.insert(key[1:])

        else:
            child.is_end = True


class WordSearch:
    """
    Module to add words to a tree and set and efficient check for matching words/ patterns
    """
    __slots__ = ['lexicon_set', 'root']
    def __init__(self):
        self.lexicon_set = set() # for exact matching
        self.root = Node()

    def add_word(self, new_word):
        """
        Add a new word to the set
        :param new_word: word to insert to the set, str
        """
        if new_word not in self.lexicon_set:
            node = self.root
            self.lexicon_set.add(new_word)
            node.insert(new_word)
            return True

        return False

    def is_word(self, my_word):
        """
        heck for exact match
        :param my_word: word to check, str
        """
        return True if (my_word.lower() in self.lexicon_set) else False

    def is_prefix(self, my_prefix):
        """
        check for words containing the prefix
        :param my_prefix: prefix to check for matches, str
        """
        node = self.root
        for char in my_prefix.lower():
            if not node.children.get(char):
                return False

            node = node.children[char]

        return True

    def get_words(self, prefix):
        """
        get all words that contain the prefix
        :param prefix: prefix to check for, str
        """
        # get the deepest node of prefix or return [] if no exists
        node = self.root
        prefix = prefix.lower()
        for char in prefix:
            if not node.children.get(char):
                return []

            node = node.children[char]

        # use the deepest prefix node to collect and return all the matches
        results = []
        self.__collect_words(node, prefix, results)
        return results

    def __collect_words(self, node, current_prefix, results):
        """
        iterate through branches of the current found prefix and
        collect words containing the prefix
        :param node: node of the current_prefix, Node
        :param current_prefix: prefix to find matching words, str
        :param results: all the matching words, list
        """
        if node.is_end:
            results.append(current_prefix)

        # use recursion to collect all the words
        for char, child in node.children.items():
            self.__collect_words(child, current_prefix + char, results)

    def get_prefix_counts(self, prefix):
        """
        Get the count of words with the matching prefix
        """
        node = self.root
        prefix = prefix.lower()
        prefix_count = 0
        for char in prefix:
            if not node.children.get(char):
                return 0
            node = node.children[char]
            prefix_count = node.num_entries

        return prefix_count