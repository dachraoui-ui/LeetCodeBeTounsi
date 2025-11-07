class Solution(object):
    
    def longestCommonPrefix(self, strs):
        prf = strs[0]
        len_prf = len(strs[0])

        for s in strs[1:] : 
            while(prf != s[0:len_prf]) :
                len_prf -=1
                if (len_prf == 0) :
                    return ""
                prf = prf[0:len_prf]

        return prf    
    

    """instead of checking each element of the array with the first one cause 
    it will be exaustive , i see that we should put the first element of array as 
    a prefix then getting this length and for each iteration for the loop 
    check the next element if it equals to the prf or not entil we get the maximum number of 
    prefixes then the prf get that maximum number and compare with the element next to it 
    """