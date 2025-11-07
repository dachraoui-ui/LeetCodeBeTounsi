class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1.remove(0)
            nums1.append(nums2[i])
        nums1.sort()

# there is a better solution than that 
    
    def merge(self, n1, m, n2, n):
        i = m - 1 
        j = n - 1 
        k = m + n - 1 
        while j >= 0 : 
            if i >= 0 and n1[i] > n2[j]:
                n1[k] = n1[i]
                i-=1
            else : 
                n1[k] = n2[j]
                j-=1
            k-=1


            