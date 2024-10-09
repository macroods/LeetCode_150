class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        num = 0

        if str1 + str2 != str2 + str1:
            return ""
        else:
            num = math.gcd(len(str1), len(str2))
            return str2[:num]