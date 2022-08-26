class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        a = nums[0]
        j = 0
        i = 1
        while i < len(nums):
            if a != nums[i]:
                
                nums[j+1] = nums[i]
                a = nums[j+1]
                j += 1
                i += 1
            else:
                i += 1
        return j+1        