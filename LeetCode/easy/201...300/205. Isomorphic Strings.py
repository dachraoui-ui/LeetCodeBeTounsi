class Solution(object):
    def isIsomorphic(self, s, t):
        map_s = []
        map_t = []
        for i in s : 
            map_s.append(s.index(i))
        for j in t : 
            map_t.append(t.index(j))
        return map_s == map_t
            
# the idea is playing with indexes at first we take the letter s and made a loop through it 
# ? for exemp : we have the letter 'egg' when we loop through it and append each index in the map_s 
# ? we got map_s = [0,1,1] why 0 1 1 and not 0 1 2 cause when searching for the index in the word s 
# it gives you the first occurence of it so the same letter don't have too indexes 
# the same for letter t and finally we compare map_s with map_t for exemp : s = 'egg' and t = 'ace' 
# map_s = [0,1,1] and map_t = [0,1,2] are not equal , a unique letter didn't map to other unique letter so 
# we return false .      