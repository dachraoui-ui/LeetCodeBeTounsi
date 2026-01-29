from typing import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        pair_list = []
        impair_list = []
        for v in count.values():
            if v % 2 == 0:
                pair_list.append(v)
            else:
                impair_list.append(v)
        if sum(impair_list) == 0 : 
            return sum(pair_list)
        else : 
            return sum(pair_list) + (sum(impair_list) - len(impair_list) + 1)