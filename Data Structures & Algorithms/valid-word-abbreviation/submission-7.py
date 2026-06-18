class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        a = 0
        b = 0
        while a < len(abbr) and b < len(word):
            if abbr[a].isdigit():
                
                if abbr[a] == '0':
                    return False
                
                num = 0
                while a < len(abbr) and abbr[a].isdigit():
                    num = num * 10 + int(abbr[a])
                    a += 1
                b += num
            else:
                if word[b] != abbr[a]:
                    return False
                a += 1
                b += 1
                
        
        return b == len(word) and a == len(abbr)