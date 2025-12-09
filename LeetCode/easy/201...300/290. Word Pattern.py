class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()
        pattern_map = []
        s_map = []
        for i in pattern :
            pattern_map.append(pattern.index(i))
        for j in s : 
            s_map.append(s.index(j)) 
        return pattern_map == s_map
     
# is the same basic like the problem 205 isomorphic Strings it fills an array with the index of pattern word 
# and the diff here between the previous prob and this is the s contains words separated by spaces 
# with O(N*M) time complexity and O(N + M) space 