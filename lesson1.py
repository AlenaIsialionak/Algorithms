from math import inf
# task1
def task1(str: str) -> str:
    res = {}
    max_value = 0
    symbol = ''
    for i in str:
        el = res.get(i)
        if el:
            res[i] = el+1

        else:
            res[i] = 1
            el = 0
        if max_value < el+1:
            max_value = el + 1
            symbol = i
    return (max_value, symbol)

# print(task1(input()))


# task2 maximum consistency

def task2(str:str) -> int:

    seq = list(map(int, str.split()))
    if len(seq) == 0:
        return '-inf'
    ans = seq[0]
    for i in seq:
        if i > ans:
            ans = i
    return ans

print(task2('1 23 4 5 21'))



