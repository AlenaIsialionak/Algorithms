class Solution:

    def isHappy(self, n: int):

        is_not_happy = set()

        while n not in is_not_happy:
            is_not_happy.add(n)
            n = sum(int(num) ** 2 for num in str(n))
            if n == 1:
                return True

        return False

result = Solution()
print(result.isHappy(19))
