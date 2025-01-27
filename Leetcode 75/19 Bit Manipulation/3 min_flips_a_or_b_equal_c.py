class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while a > 0 or b > 0 or c > 0:
            last_a = a & 1
            last_b = b & 1
            last_c = c & 1

            # need to make both 0
            if last_c == 0:
                flips += last_a + last_b

            # last_c == 1
            # need to make any one of them 1
            else:
                if last_a == 0 and last_b == 0:
                    flips += 1

            # right-sihft by 1 to check next bit
            a = a >> 1
            b = b >> 1
            c = c >> 1

        return flips
