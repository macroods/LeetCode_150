class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        s_reverse = []

        for n in range(len(s_list) -1, -1, -1):
            s_reverse.append(s_list[n])
            if n != 0:
                s_reverse.append(' ')

        return ''.join(s_reverse)
