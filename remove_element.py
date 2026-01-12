from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0 # this is the reference place index inside the nums
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i
    
user_input=list(map(int,input("Enter the list : ").split()))
val=int(input("enter the value"))
sol=Solution()
print(f"{sol.removeElement(user_input,val)}")