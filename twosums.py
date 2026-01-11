from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}  # value -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], i]
            prev[n] = i

user_input = list(map(int, input("Enter the numbers separated by space: ").split()))

target=int(input("Enter the Target: "))
sol=Solution()
result=sol.twoSum(user_input,target)
print(result)