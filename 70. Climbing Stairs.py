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