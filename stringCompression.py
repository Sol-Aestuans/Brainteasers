class Solution:
  def compress(self, chars: list[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      
      ## count duplicates
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[ans] = letter
      ans += 1

      ## encode numbers
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1
        
        # remove duplicate chars and adjust i
        j = ans
        while j < len(chars) and chars[j] == letter:
          chars.pop(j)
          i-=1

    return ans
if __name__ == "__main__":
    chars = ["a","a","b","b","b","b","b","b","b","b","b","b","b"]
    result = Solution().compress(chars)
    print("String: " + "".join(chars) + "\nCompressed length:" + str(result))