"""
LinkedIn: https://www.linkedin.com/in/mochi-momo/
github: https://github.com/mochi-momo
YouTube: https://www.youtube.com/channel/UCn2KHtlnvJNd3oRqH7tMjkg
email: emailtomohitsingh@gmail.com
Instagram: @mohit_was_here
"""
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{', ']':'['}
        open_brackets=[]
        for char in s:
            if char in brackets.values():
                open_brackets.append(char)
            elif open_brackets and brackets[char] == open_brackets[-1]:
                open_brackets.pop()
            else: return False
        return open_brackets == []
