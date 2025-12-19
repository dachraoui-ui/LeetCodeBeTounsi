class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        fst = 0 
        end = num 
        while (fst <= end ):
            mid = (fst + end) // 2
            if mid * mid  > num :
                mid -=1
                end = mid
            elif mid * mid  < num :
                mid+=1
                fst = mid 
            else : 
                return True 
        return False
# this solution uses binary search it's simple approach but it's hard to think of it 
# starting like any normal binary search but instead of only mid we use mid² cause we should 
# check if that mid power 2 is greater than the num or not if greater we goes to the left 
# if less we goes to right and make it bigger .
# this solution have O(log(n)) time , and O(1)  no extra space 
# log n cause each time we get smaller part to search on it 