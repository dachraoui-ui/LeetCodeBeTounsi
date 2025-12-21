from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_ran = Counter(ransomNote) 
        cnt_mag = Counter(magazine)
        for c in cnt_ran : 
            if not((c in cnt_mag) and (cnt_ran[c] <= cnt_mag[c])):
                return False 
        return True 
     
