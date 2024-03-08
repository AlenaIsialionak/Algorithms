def task1(str_: str) -> str:
    res = ''
    count = 0
    for i in range(len(str_)):
        if not res:
            res += str_[i]
            count += 1
            continue

        if len(str_) - 1 == i:
            if count > 1:
                res += str(count)

        if str_[i-1] == str_[i]:
            count += 1
        else:
            if count > 1:
                res += str(count)
            count = 0
            res += str_[i]
            count += 1

    return res



class Solution:

    def pack(self, symbol, count):
     if count > 1:
         return symbol + str(count)
     return symbol

    def task(self, s: str):
        last_sym, last_pos = s[0], 0
        res = []
        for i in range(len(s)):
            if s[i] != last_sym:
                res.append(self.pack(last_sym, i - last_pos))
                last_sym, last_pos = s[i], i
        res.append(self.pack(last_sym, len(s) - last_pos))

        return ''.join(res)


sol = Solution()
print(sol.task('a'))