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

    
        # ? Solution 2 : 
        # here using a single loop and using the logic of substracting the target number 
        # from the number of the array , and search if the target - num[i] available in array or not 
        # O(n²) time complexity 
        
        for i in range (len(nums)) :
            if(target - nums[i] in nums[:i] + nums[i+1:] ):
                if(nums[i] == target - nums[i] ) :
                    return i , nums.index(target -nums[i] , i + 1)
                else : 
                    return i, nums.index(target-nums[i]) 



        # ? thrid solution 3 : 
        """To avoid using 2 loops and O(n²) we use the hashMap so at first initializing 
        the map so when putting values on it we can access them by the key or value 
        instantly so that reduce the O(n²) to O(n) .

        The enumrate function that let me loop through a list giving me the index and the values 
        X is the differance between target and num 
        the if condition search for the key x in the hashMap cause when searching like that in hashMap we 
        search by the key after that we check if that key exist in the hashMap if yes return the index 
        of the element in the real list and the index of the x number in the hashMap (value) .
        the final step is when the if condition is false that key <--- value (i) (index)
    """
        hashM = {} 
        for i , num in enumerate(nums) : 
            x = target - num 
            if x in hashM : 
                return i, hashM[x]
            hashM[num] = i