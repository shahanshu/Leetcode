from typing import List
class solutions:
    
    def singleNumber(self,nums:List[int]) -> int:
        answer=0
        for n in nums:
            answer^=n
        return answer
    
sol=solutions()
result=sol.singleNumber(nums=[4,3,3,4,7])
print(result)