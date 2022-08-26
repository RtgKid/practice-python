class Solution:
    def isHappy(self, n: int) -> bool:
        while len(str(n)) != 1:
            l = list(str(n))
            n = sum([int(i)* int(i) for i in l])
            print(n)
        if n == 1 or n == 7:
            return True
        else:
            return False