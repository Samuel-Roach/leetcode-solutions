class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        correct_words = []

        for word in words:
            mapping = {}
            word_letters_matched = []
            correct = True

            for idx, letter in enumerate(word):
                if (pattern[idx] in mapping and mapping[pattern[idx]] != letter) \
                    or (letter in word_letters_matched and pattern[idx] not in mapping):
                    correct = False
                else:
                    mapping[pattern[idx]] = letter
                    word_letters_matched.append(letter)

            if correct:
                correct_words.append(word)
        return correct_words
