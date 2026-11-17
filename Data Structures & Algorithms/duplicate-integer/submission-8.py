class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #einmal mit array
        list_arr=[]

        for n in nums:
            if n in list_arr:
                return True
            list_arr.append(n)
        return False