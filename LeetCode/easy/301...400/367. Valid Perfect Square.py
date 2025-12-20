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

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num
        while (x * x > num) :
            x = (x + num // x) // 2
        return x * x == num
    
# now a pure mathematical solution using Newton method raphson for more undrestanding
# visit : https://en.wikipedia.org/wiki/Newton%27s_method
# in sumary this newton method using the formula (x + num // x) // 2
# to each time get the best approximate for the root of that number 
# the main idea is like that and finally we return if the end result power 2 equal to num it self 
