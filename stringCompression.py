class Solution:
    def compress(self, chars) -> int:

        running_total = 1

        for i in range(0, len(chars)):
            cur = chars[i]
            if len(chars) == 0 or isinstance(chars[i-1], int) or output[-1] != cur:
                output.append(cur)
            elif cur == output[-1]:
                running_total += 1
            if i == len(chars) - 1 or chars[i + 1] != cur:
                running_total_str = str(running_total)
                if len(running_total_str) > 1:
                    for char in running_total_str:
                        output.append(char)
                elif running_total > 1:
                    output.append(str(running_total))
                running_total = 1
                
        return output

if __name__ == "__main__":
    chars = ["a","a","b","b","b","b","b","b","b","b","b","b","b"]
    sol = Solution()
    result = sol.compress(chars)
    print("Compression string: ", result)
