class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        absoluteMin = secondMin = float('inf')
        for n in nums:
            if n <= absoluteMin: absoluteMin = n
            elif n <= secondMin: secondMin = n
            else: return True
        return False

if __name__ == "__main__":
    print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))