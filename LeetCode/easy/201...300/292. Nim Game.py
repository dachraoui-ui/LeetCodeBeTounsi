class Solution(object):
    def canWinNim(self, n):
        return n % 4 != 0
     
# this problem seems hard but when dig through the test case from 1 to 8 and test it manually 
# the solution will appear at first we have that 1 , 2 , 3 are true and when we go to 4 we get 
# false, the first half of the parttern appear now test from 5 to 8 to confirme the pattern 
# so when we test 5 , 6 and 7 we got true but it stops in 8 , now you start thinking at first 4 and now 8 
# it should be a relation that the number shouldn't be the multiply of 4 to win the game .
# why 4 : the topic said that you can move by 1,2 or 3 and when reaching the 4 no matter what you do you choose 1 , 2 or 
# 3 to start you lose .