from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        if len_s1 > len_s2:
            return False
        
        c1 = Counter(s1)
        c2 = Counter(s2[:len_s1])  
        
        if c1 == c2:
            return True
        
        for i in range(len_s1, len_s2):
            c2[s2[i]] += 1
            
            c2[s2[i - len_s1]] -= 1
            
            if c2[s2[i - len_s1]] == 0:
                del c2[s2[i - len_s1]]
            if c1 == c2:
                return True
        
        return False
