from typing import List


class Solution:
    def searchInsert1(self, nums, target):
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            mid = (left + right) // 2
        return left

    def searchInsert2(self, nums: List[int], target: int) -> int:
        for a, b in enumerate(nums):
            if target == b or target < b:
                return a
        return len(nums)


    def finfMin(self, nums):


        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return (left, nums[left])
        div = nums[0]
        mid = (left + right) // 2


        while nums[mid] > nums[mid-1] and right>1:
            if nums[mid-1] < nums[mid] and div < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

            # if right - left == 1:
            #     return right

            mid = (left + right) // 2
            if mid == 0:
                return right, nums[right]

        return (mid, nums[mid])



    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l, r = max(weights), sum(weights)
        res = r


        def haveCapascity(cap):
            cur = cap
            countDays = 1

            for weight in weights:
                if cur - weight < 0:
                    countDays += 1
                    cur = cap

                cur -= weight

            return countDays if countDays <= days else None

        while l <= r:

            cap = (l + r) // 2

            if haveCapascity(cap):
                res = min(cap, res)
                r = cap - 1

            else:
                l = cap + 1

        return res


    def search(self, nums: List[int], target):

        l, r = 0, len(nums) - 1



        while l <= r :
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1



print(Solution().search([4,5,6,7,0,1,2], 6))

# print(Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))

# print(Solution().searchInsert1([1, 3, 5, 6], 7)

# print(Solution().finfMin([5, 1, 2, 3, 4]))
# print(Solution().finfMin([3,4,5,1,2]))