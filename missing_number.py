from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen=set(nums)
        ans=set()
        for i in range(1,len(nums)+1):
            if i not in seen:
                ans.add(i)
        return list(ans)