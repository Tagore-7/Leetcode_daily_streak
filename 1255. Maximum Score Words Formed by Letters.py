class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_count = Counter(letters)
        print(letter_count)
        no_of_words = len(words)
        print(no_of_words)
        maximum_score = 0
        for i in range(1 << no_of_words):
            current_word_count = Counter("".join(words[j] for j in range(no_of_words) if (i >> j) & 1))
            print(current_word_count)

            if all(current_word_count[letter] <= letter_count[letter] for letter in current_word_count):
                current_score = sum(current_word_count[letter] * score[ord(letter) - ord('a')] for letter in current_word_count) 
                print(current_score)
                maximum_score = max(maximum_score, current_score)
                print(maximum_score)

        return maximum_score
