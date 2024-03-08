def longestPalindrome(s: str) -> str:
    lengthRes = 0
    res = ''
    for i in range(len(s)):
        # for odd
        l, r = i, i
        res, lengthRes = conditional(s, l, r, lengthRes, res)

        # for even
        l, r = i, i+1

        res, lengthRes = conditional(s, l, r, lengthRes, res)

    return res

def conditional(s, l, r, lengthRes, res):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if r - l + 1 > lengthRes:
            res = s[l: r + 1]
            lengthRes = r - l + 1
        l -= 1
        r += 1
    return res, lengthRes

# print(longestPalindrome('babad'))


class Solution:

    def countSubstrings(self, s: str) -> int:

        count = 0

        for i in range(len(s)):

            l, r = i, i
            count = self.conditional(s, l, r, count)


            l, r = i, i + 1

            count = self.conditional(s, l, r, count)

        return count

    def conditional(self, s, l, r, count):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        return count


result = Solution()

print(result.countSubstrings('aaa'))