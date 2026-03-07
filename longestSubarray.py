class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        result = left = zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros +=1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -=1
                left += 1
            result = max(result, right - left)
            
        return result
    
if __name__ == "__main__":
    nums = [1,1,1]
    sol = Solution()
    print(sol.longestSubarray(nums))