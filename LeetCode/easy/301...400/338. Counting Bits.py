from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        list_1 = []
        for i in range(n+1):
            list_1.append(bin(i).count("1"))
        return list_1
     
# solution with time complexity O(n log n) that for every index count how many ones 

class Solution:
    def countBits(self, n: int) -> List[int]:
        list1 = [0]*(n+1)
        max_p2 = pow(2,13)
        for i in range(1,n+1):
            if max_p2 % i == 0 : 
                list1[i] = 1
            else : 
                list1[i] = list1[i//2] + (i % 2)
        return list1

# now this solution with linear time O(n) 
# at first we made an array with length n + 1 then make a loop with that range 
# we have also made the max_p2 to check if that number is power of 2 or not so we put 
# one if not the current index get the i // 2 so we element the last bit and if the number 
# is even i % 2 == 0 and if it's odd it's 1 try the execution and you will see  