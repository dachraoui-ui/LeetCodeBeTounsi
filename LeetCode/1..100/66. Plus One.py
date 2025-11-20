class Solution(object):
    def plusOne(self, digits):
        new =[]
        power = len(digits) -1
        s = 0
        for i in range(len(digits)):
            s = s + digits[i] * pow(10,power)
            power-=1
            
        s+=1
        new = map(int,str(s))

        return new

# there is a better one i think 