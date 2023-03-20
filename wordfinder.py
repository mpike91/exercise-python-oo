"""Word Finder: finds random words from a dictionary."""

from random import choice


class WordFinder:
    """Finds a word from a list of words read from a file.

    >>> wf = WordFinder("wordsTest.txt")
    7 words read.

    """

    def __init__(self, path):
        """Initializes words list and then prints number of words read."""
        self.words = self.createWordList(path)
        print(f"{len(self.words)} words read.")

    def createWordList(self, path):
        """Opens file from the passed "path", passes it to loopList to generate the list, closes the file, and returns word_list."""
        file = open(path, "r")
        word_list = [w.strip() for w in file]
        file.close()
        return word_list

    def random(self):
        """Returns a random element from the words list."""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Subclass of WordFinder"""

    def random(self):
        """Updated random() to "catch" any blank lines or commented lines using a while loop."""
        from random import choice
        random_word = ""
        while random_word.startswith("#") or not random_word:
            random_word = choice(self.words)
        return random_word
