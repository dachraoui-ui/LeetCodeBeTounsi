class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alph = [0]*26
        for i in s :
            alph[ord(i) - 97] +=1
        for j in t : 
            alph[ord(j) - 97] -=1
        for k in range(26) : 
            if alph[k] == -1:
                return chr(k + 97)

# this solution depends on creating another table that contains 0 and 26 cases for the number of letters in 
# alphbet , for the first loop we loop through the letter 's' and each time we get a letter we go to alph array 
# and add 1 for the index of that letter 
# for the second loop each time we check a letter in t if it exist in alph we sub 1 tell we got one letter 
# with -1 and this is the missing letter 
