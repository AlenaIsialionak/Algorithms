# def func(value: int, l: list[int] = None):
#     if l is None:
#         l = []
#     l.append(value)
#     return l
#
#
# print(func(3))
# print(func(5))
# print(func(4, [9, 9]))
#
# set

setsize = 10
myset = [[] for _ in range(setsize)]

def add(x):
    if not find(x):
        myset[x % setsize].append(x)


def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
        return  False

def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i]
            xlist.pop()
            return



# task (1, 2, 3, 5) = target = 7 result = 2, 5, if target = 10 result = False

def twotermswitchsumx(nums: list , target: int) -> tuple:
    prev = set()
    for num in nums:
        if target - num in prev:
            return num, target - num
        prev.add(num)
    return False

print(twotermswitchsumx([1, 2, 3, 4, 5], 9))

