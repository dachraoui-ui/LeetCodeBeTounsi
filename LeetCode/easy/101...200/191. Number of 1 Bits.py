class Solution(object):
    def hammingWeight(self, n):
        binary = bin(n)[2:]
        count =0
        for i in binary : 
            if i == '1':
                count+=1
        return count

# easy solution no need to explain only i will explain the bin fonction that convert the number to a binary 
# like '0b11101' to string binary and then we slice it to delete the first two caracter cause they are not 
# belong the binary format 
        
        