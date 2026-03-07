class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_vowels = 0
        current_count = 0

        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_vowels = max(max_vowels, current_count)

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1
            max_vowels = max(max_vowels, current_count)
        return max_vowels
    
if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    print(Solution().maxVowels(s, k))