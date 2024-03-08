from typing import List
from logger import logger


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f'Called {func.__name__} with args {args} and kwargs {kwargs}')
        result = func(*args, **kwargs)
        logger.info(f'{func.__name__} returned result')
        return result
    return wrapper


class Solution:

    @logging_decorator
    def rob_1(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for i in nums:
            temp = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    @logging_decorator
    def rob_2(self, nums: List[int]) -> int:

        return max(nums[0] ,self.rob_1(nums[1:]), self.rob_1(nums[:-1]))


result = Solution()


print(result.rob_1([1, 2, 3, 1]))
print(result.rob_2([1,2,3,1]))
