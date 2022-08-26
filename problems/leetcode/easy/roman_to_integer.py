class Solution:
    
    def romanToInt(self, s: str) -> int:
        d = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000}
    
        sm = 0
        i = 0
        while i < len(s) - 1:
            print(i)
            if s[i] == 'I':
                if s[i+1] == 'V':
                    sm += 4
                    i += 1
                elif s[i+1] == 'X':
                    sm += 9
                    i += 1
                else:
                    sm += d[s[i]]
            
            elif s[i] == 'X':
                if s[i+1] == 'L':
                    sm += 40
                    i += 1
                elif s[i+1] == 'C':
                    sm += 90
                    i += 1
                else:
                    sm += d[s[i]]
                    
            elif s[i] == 'C':
                if s[i+1] == 'D':
                    sm += 400
                    i += 1
                elif s[i+1] == 'M':
                    sm += 900
                    i += 1
                else:
                    sm += d[s[i]]        
            else:
                sm += d[s[i]]   
            i += 1
            
        if s[-2:] not in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            sm += d[s[-1]]
        return sm     