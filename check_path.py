#
# def check_path(path):
#     if not path:
#         return '/'
#     new_path = path.replace('.//', '').split('/')
#     result_path = []
#     for i in new_path:
#         if i != '..':
#             result_path.append(i)
#         else:
#             if result_path:
#                 result_path.pop()
#             else:
#                 result_path.append('')
#     return '/'.join(result_path)
#
#
# assert check_path('/foo/bar/../test/../test/../baz/.//bar') == '/foo/baz/bar'
# assert check_path("") == '/'
# assert check_path('../.././/../') == '/'
#
from collections import deque
# #
# def slidingwindow(array: list, k: int ):
#     if not array or len(array) == 1 or k == 1:
#         return array
#     window = deque()
#     arr = deque(array)
#     max_arr = []
#     for _ in range(k):
#         window.append(arr.popleft())
#     while window:
#         if len(window) == k:
#             max_elem = window.popleft()
#         window_left = deque()
#         for i in window:
#             if i > max_elem:
#                 max_elem = i
#                 window_left = deque([i])
#             else:
#                 window_left.append(i)
#         max_arr.append(max_elem)
#         window = window_left
#         if not arr:
#             break
#         window.append(arr.popleft())
#
#
#
#
#
#     return max_arr
#
# print(slidingwindow([7, 2, 4], 2)) # [7, 4]
# print(slidingwindow([-7, -8, 7, 5, 7, 1, 6, 0], 4)) # [7,7,7,7,7]
# print(slidingwindow([1, 3, 1, 2, 0, 5], 3)) # [3,3,2,5]




# def slidingwindow(nums: list, k: int ):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: List[int]
#     """
#     d = deque()
#     out = []
#     for i, n in enumerate(nums):
#         # print("i = {}, curr element = {}, d = {} and out = {}".format(i, n, d, out))
#         while d and nums[d[-1]] < n:
#             # print(nums[d[-1]])
#             d.pop()
#             # print("\t Popped from d because d has elements and nums[d.top] < curr element")
#         d.append(i)
#         # print("\t Added i to d")
#         if k == i - d[0]:
#             d.popleft()
#             # print("\t Popped left from d because it's outside the window's leftmost (i-k)")
#         if i >= k - 1:
#             out.append(nums[d[0]])
#             # print(f'out{nums[d[0]]}')
#             # print("\t Append nums[d[0]] = {} to out".format(nums[d[0]]))
#
#
#     return out
#
#
# print(slidingwindow([7, 2, 4], 2)) # [7, 4]
# print(slidingwindow([],k=0))
#
# print(slidingwindow([-7, -8, 7, 5, 7, 1, 6, 0], 4)) # [7,7,7,7,7]
# print(slidingwindow([1, 3, 1, 2, 0, 5], 3)) # [3,3,2,5]
# print(slidingwindow([9,10,9,-7,-4,-8,2,-6], 5)) # [10, 10, 9, 2]



# def power(x, n):
#     if x == 0:
#         return 0
#     else:
#         result = 1
#         if n >= 0:
#             while n != 0:
#                 if n%2 == 0:
#                     x = x*x
#                     n = n//2
#                 else:
#                     result = result*x
#                     n = n-1
#             return result
#         else:
#             n = -n
#             while n != 0:
#                 if n % 2 == 0:
#                     x = x*x
#                     n = n // 2
#                 else:
#                     result = result * x
#                     n = n - 1
#             return 1/result
#
# print(power(2, -5))



    # def wordbreak(s, arr):
    #     for i in arr:
    #         s = s.replace(i, '')
    #     if not s:
    #         return True
    #
    #     return False
    #
    # print(wordbreak('leetcode',['leet','code']))
    #
    #
    #
    #
    # def gen(n):
    #     count = 0
    #     for i in range(n):
    #         count+=1
    #         yield (i, count)
    #
    #
    #
    # for i in gen(5):
    #     print(i)
    #

def my_decorator1(func):
    def wrapper(*args, **kwargs):
        print("Inside decorator 1.")
        func(*args, **kwargs)

    return wrapper

def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print("Inside decorator 2.")
        func(*args, **kwargs)

    return wrapper

@my_decorator1
@my_decorator2
def my_function():
    print("Inside the function.")

my_function()

