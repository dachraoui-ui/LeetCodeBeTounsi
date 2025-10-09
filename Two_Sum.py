class Solution(object):
    def twoSum(self, nums, target):
        
        # ? solution 1 : brute force 
        
        # this is a basic solution using nested loop , using two pointers 
        # one after the others to avoid the duplication of numbers and indexes 
        # !! time complexity O(n²) cause we're using nested loop and memory O(1) cause we don't use any extra space 

        for i in range (len(nums)) :
            for j in range(len(nums)) :
                if(nums[j] + nums[i] == target and i != j ) : 
                    return i , j 

    
        # Solution 2 : 
        # here using a single loop and using the logic of substracting the target number 
        # from the number of the array , and search if the target - num[i] available in array or not 
        # O(n²) time complexity 
        
        for i in range (len(nums)) :
            if(target - nums[i] in nums[:i] + nums[i+1:] ):
                if(nums[i] == target - nums[i] ) :
                    return i , nums.index(target -nums[i] , i + 1)
                else : 
                    return i, nums.index(target-nums[i]) 

