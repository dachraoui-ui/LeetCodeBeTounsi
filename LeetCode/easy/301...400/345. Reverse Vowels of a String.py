class Solution:
    def reverseVowels(self, s: str) -> str:
        vowl = {'a','e','i','o','u','A','E','I','O','U'}
        lst = list(s)
        aux =''
        i = 0
        j = len(s) -1
        while ( i < j ) :
            if lst[i] in vowl : 
                if lst[j] in vowl : 
                    aux = lst[i]
                    lst[i]=lst[j]
                    lst[j] = aux
                    j-=1
                    i+=1
                else : 
                    j-=1
            elif lst[j] in vowl : 
                if lst[i] in vowl : 
                    aux = lst[i]
                    lst[i]=lst[j]
                    lst[j] = aux
                    j-=1
                    i+=1
                else : 
                    i+=1
            else :
                i+=1
                j-=1
        return ''.join(lst)
     
#  run time O(n) , space O(n)
# the principe in solution is two pointers one in the beginning and one in the end 
# and every time we check if lst[i] is vowel then check if lst[j] is vowel in nested if , if not j-- if yess we 
# permut i and j and i++ and j-- , and the same approch for the second if but switching i by j 