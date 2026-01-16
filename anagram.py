class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)== sorted(t)
    """
     or we can use the counter that returns the stinrgs with the frequency as the key value pair respectively
     
     return counter (s)== counter(t)
    """