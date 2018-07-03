# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        b = []
        for i in s:
            if i not in b:
                b.append(i)
        s = [ x for x in s]

        x1 = []
        x2 = []
        for i in b:
            count = 0
            for j in s:
                if j == i:
                    count += 1

            x1.append(i)
            x2.append(count)

        if 1 not in x2:
            return -1
        else:
            for i in range(0, len(x2)):
                if x2[i] == 1:
                    break
            for j in range(0, len(s)):
                if s[j] == x1[i]:
                    break
            return j

s = Solution()
a = 'NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp'
b = 'google'
print s.FirstNotRepeatingChar(a)