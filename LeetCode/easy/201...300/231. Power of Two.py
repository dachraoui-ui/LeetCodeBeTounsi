class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n_bin = bin(n)[2:]
        return n_bin.count("1") < 2 and n > 0

# when think in this problem as programmer or you are a fresh student that still studing in the university 
# the solution will instantly comes goes will all now that the binary numbers no matter the numbers of bits 
# we now that each bit from the right to the left increase by the power of 2 that's why we convert the number to 
# binary and check if it's positive and have only one "1"     