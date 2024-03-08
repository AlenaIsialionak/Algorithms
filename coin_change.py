from typing import List
import math


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [math.inf] * (amount+1)
#         dp[0] = 0
#         for a in range(1, amount + 1):
#             for c in coins:
#                 if a-c >= 0:
#                     dp[a] = min(dp[a], 1 + dp[a-c])
#         return dp[amount] if dp[amount] else -1


# res = Solution()
# print(res.coinChange([3, 4, 5], 11))

res = [x**2 for x in [1, 2, 3]]
m = map(lambda x: x**2, [1, 2, 3])



class Solution:

    def coin_change(self, coins: List[int], amount) -> int:
        dp = (amount+1)*[amount+1]
        dp[0] = 0

        for each_amount in range(1, amount+1):
            for coin in coins:
                if each_amount - coin >= 0:
                    dp[each_amount] = min(dp[each_amount], 1 + dp[each_amount - coin])

        return dp[amount] if dp[amount] != amount+1 else -1

    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        min_sub, max_sub = 1, 1
        for num in nums:
            temp = max_sub
            max_sub = max(num * max_sub, num*min_sub, num)
            min_sub = min(num * min_sub, temp*num, num)
            res = max(max_sub, res)

        return res



res = Solution()
print(res.coin_change([2], 3))
print(res.maxProduct([2, 3, -2, -4]))