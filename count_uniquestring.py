from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        time=Counter(s)
        for i,val in enumerate(s):
            if time[val]==1:
                
                return i
        return -1
