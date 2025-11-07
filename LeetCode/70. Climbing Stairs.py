class Solution(object):
    
   # i think of fibonacii solution but it has a time complexity of O(2 power(n)) and space complexity of O(n)
    def climbStairs(self, n):
        def Fibonacci(n) :
            if n == 0 :
                return 1
            elif n < 0 :
                return 0
            
            return Fibonacci(n - 1) + Fibonacci(n - 2)
        return Fibonacci(n)
    

   # to get the actual number n we start from the beginning (start climbing the stairs) so the first obvious n result and 
   # those we will start with are 1 and 2 , by making stp1 and stp2 as 2 and 1 , as the Fibonacci principle said that 
   # the next element is the sum of the two previous element so we will start from the 3 and so on and if we want to get the 
   # steps for 5 we count at first the sum of two previous 3 and 4 and the logic behind the loop proves everything 
    def climbStairs(self, n):
        if n == 1 or n == 2 : 
            return n
        stp1 = 2 
        stp2 = 1
        for _ in range (3 , n + 1):
            sum = stp1 + stp2
            stp2 = stp1
            stp1 = sum 
        return stp1