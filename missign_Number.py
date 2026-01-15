from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=set(nums)
        '''
         here why did we created the set of the nums cause we don't need the order and 
         Instead of checking a list every time (slow)
         Now membership is constant time.
        '''
        for i in range(len(n)+1):
            if i not in n:
                return i