class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_seen=set(jewels)
        
        c=0
        for i in stones:
            if i in j_seen:
                c+=1
        return c