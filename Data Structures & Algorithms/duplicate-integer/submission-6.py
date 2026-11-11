class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_list=[]

        for index in range(len(nums)):
            if nums[index] in my_list:
                return True
            else:
                my_list.append(nums[index])
                
        return False