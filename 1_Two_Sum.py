class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        temp = 0
        newNums = []

        for num in range(0, len(nums)):
            temp = nums[num]
            for i in range(num+1, len(nums)):
                if temp + nums[i] == target:
                    newNums.append(num)
                    newNums.append(i)
                    return newNums