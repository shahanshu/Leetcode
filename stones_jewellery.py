class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_seen=set(jewels)
        
        
        return sum(1 for c in stones if c in j_seen)