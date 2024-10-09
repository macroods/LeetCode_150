class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        answer = [1] * len(nums)

        for n in range(1, len(nums)):
            left[n] = left[n-1] * nums[n-1]

        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for m in range(len(nums)):
            answer[m] = left[m] * right[m]
        
        return answer