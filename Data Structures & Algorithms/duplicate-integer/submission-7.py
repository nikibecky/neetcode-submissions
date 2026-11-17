class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #einmal mit Hashlist
        Seen=set()

        for n in nums:
            if n in Seen:
                return True 
            Seen.add(n)  
        return False
