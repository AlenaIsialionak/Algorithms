d = {
    'a': 34,
    'b': 66,
    'c': 12,
    'd': 9000,
}
print(d['a'], d.get('a'))

def two_max(d: dict):
    max1, max2 = None, None
    key1, key2 = None, None
    for key, item in d.items():
        if max1 is None:
            max1 = max2 = item
            key1 = key2 = key
            continue
        else:
            if max1 < item:
                max1, max2 = item, max1
                key1, key2 = key, key1
                continue
            if max2 < item:
                max2 = item
                key2 = key

    return (max1, max2), (key1, key2)

print(two_max(d))


l = [1, 2, 3, 4, 5]
print(l[-2:])






