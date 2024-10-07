class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        s_list = list(s)

        for n in range(len(s_list)):
            if s_list[n] in ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'):
                vowels.append(s_list[n])
                s_list[n] = 1
        
        for m in range(len(s_list)):
            if s_list[m] == 1:
                s_list[m] = vowels.pop()
        
        return ''.join(s_list)