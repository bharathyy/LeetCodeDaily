class Solution:
    def minLength(self, s: str) -> int:
        word = s
        while True:
            initial_length = len(word)
            word = word.replace("AB", "").replace("CD", "")
            if len(word) == initial_length:
                break

        return len(word)