class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        length = min(len(word1), len(word2))

        for letter in range(length):
            merged.append(word1[letter])
            merged.append(word2[letter])
    
        merged.append(word1[length:])
        merged.append(word2[length:])

        return ''.join(merged)