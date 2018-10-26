class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
       
        while(first < len(nums)):
            spclNum = target - nums[first]
            if(spclNum in nums and first != nums.index(spclNum)):
                spclIndex = nums.index(spclNum)
                return [first, spclIndex]
            else:
                first += 1