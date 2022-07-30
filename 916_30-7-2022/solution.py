import enum


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        def letter_count(word):
            letters = [0] * 26
            for letter in word:
                letters[ord(letter) - ord('a')] += 1
            return letters

        bmax = [0] * 26

        for subset in words2:
            for idx, letter in enumerate(letter_count(subset)):
                if bmax[idx] < letter:
                    bmax[idx] = letter

        universal_words = []

        for word in words1:
            universal = True

            for idx, letter in enumerate(letter_count(word)):
                if letter < bmax[idx]:
                    universal = False

            if universal:
                universal_words.append(word)

        return universal_words