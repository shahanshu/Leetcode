from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        i=0     #here we need a reference that should be compared to the rest of the values 
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]: #check the new element to the previous ones 
                i=i+1
                nums[i]=nums[j]
        return i+1
    # split is used inside the map functions 
user_input = list(map(int, input("Enter numbers separated by space: ").split()))
so=Solution()
result=so.removeDuplicates(user_input)
print(result)