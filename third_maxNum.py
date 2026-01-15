from typing import List

class solution:
    def max(self,num:list[int])-> int:
        seen=set(num)
        num2=sorted(list(seen),reversed=True)
        if len(num2)<3:
            return num2[0]
        return num2[2]