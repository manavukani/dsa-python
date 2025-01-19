# Input: chars = ["a","a","b","b","c","c","c"]
# Output: 6
# Explanation: at end input array should be: ["a","2","b","2","c","3"], that is it needs 6 chars

# TC = N
# SC = const. --> requirement
class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        left = 0

        for right in range(1,len(chars)+1):
            # skips repeating char
            if right < len(chars) and chars[right-1] == chars[right]:
                count += 1
            else:
                # end of repeating char @ left
                chars[left] = chars[right-1]    
                left += 1
                # count greater than 1 then only write the number
                if count > 1:
                    for c in str(count):
                        chars[left] = c
                        left += 1
                # reset count
                count = 1

        return left