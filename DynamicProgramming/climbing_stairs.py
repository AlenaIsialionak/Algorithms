from typing import List


class Solution:
    """
    Fibonacci Number
    """
    def climbing_stairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            prev = one
            one = one + two
            two = prev

        return one

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        one, two = 1, 0

        for i in range(n-1):
            prev = one
            one = one + two
            two = prev

        return one


    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])

solved = Solution()

print(solved.fib(0))
print(solved.minCostClimbingStairs([1,11]))
