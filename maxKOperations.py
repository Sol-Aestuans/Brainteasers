class Solution:
    def maxOperations(self, nums: list[int], k:int) -> int:
        left, right, sum, max_ops = 0, len(nums) - 1, 0, 0
        nums.sort()
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                left+=1
                right-=1
                max_ops+=1
            elif sum > k:
                right-=1
            else:
                left+=1

        return max_ops
    
if __name__ == "__main__":
    sol = Solution()
    k = 4
    nums = [2,2,2,3,1,1,4,1]
    print(sol.maxOperations(nums, k))