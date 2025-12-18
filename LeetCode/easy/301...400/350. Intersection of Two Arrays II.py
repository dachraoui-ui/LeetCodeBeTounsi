from typing import List
from collections import Counter

class Solution:
    def intersect(self, n1: List[int], n2: List[int]) -> List[int]:
        res = []
        for i in range(len(n1)):
            if n1[i] in n2 :
                res.append(n1[i])
                n2.remove(n1[i])
        return res
     
# the first solution with O(n * m) time complexity and O(1) space complexity 

class Solution:
    def intersect(self, n1: List[int], n2: List[int]) -> List[int]:
        c1 = Counter(n1)
        c2 = Counter(n2)
        res = []
        for key in c1 : 
            if key in c2 :
                for _ in range(min(c1[key],c2[key])):
                    res.append(key)
        return res 
     
# in this approach we have better solution with O(n + m) time complexity 
# O(n + m ) space complexity : 
# in this approach we make 2 counter , counter are hashtable that counts the appeariance of an 
# element so the key is the element and the value is the number of his appearance 
# second : for each key in c1 we check if that key is available in c2 and if yes we make a loop 
# to right n time the appearance of that number so we use the min function so we get exactally the number 
# of appearance in both of them and finally we append each time to res 
    