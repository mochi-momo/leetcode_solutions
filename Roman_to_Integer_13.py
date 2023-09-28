"""
LinkedIn: https://www.linkedin.com/in/mochi-momo/
github: https://github.com/mochi-momo
email: emailtomohitsingh@gmail.com
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} # dictionary with values
        total = 0
        
        #run through each character of input
        #if value is less than the value that comes afterwards subtract, else add
        for x in range(len(s)):
            if x+1 < len(s) and numerals[s[x]] < numerals[s[x+1]]:
                total -= numerals[s[x]]
            else:
                total += numerals[s[x]]
        
        return total
