class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)) :
            if target == nums[i] :
                return i
            else : 
                nums.append(target)
                nums.sort()
                return nums.index(target)
            
#there is a better one 
        