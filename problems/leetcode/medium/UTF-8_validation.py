class Solution:
    def num_of_ones(self, s : str) -> int:
        c = 0
        for i in s:
            if i == '1':
                c += 1
            else:
                return c
        return c            
            
    def validUtf8(self, data) -> bool:
        bin_data = [str(format(i, '#010b'))[2:] for i in data]
        should_start_with_10 = False
        k = 0
        for i in bin_data:
            if k == 0:
                k = self.num_of_ones(i)
                if k == 0:
                    continue
                if k == 1:
                    return False
                else:
                    k = k - 1    
            else:
                if not i.startswith('10'):
                    return False
                else:
                    k -= 1

        return k == 0
                


                
s = Solution()
print(s.validUtf8([250,145,145,145,145]))
print(s.validUtf8([240,162,138,147,145]))
print(s.validUtf8([197,130,1]))
print(s.validUtf8([235,140,4]))
print(s.validUtf8([230,136,145]))