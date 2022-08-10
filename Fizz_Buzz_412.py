"""
LinkedIn: https://www.linkedin.com/in/mochi-momo/
github: https://github.com/mochi-momo
YouTube: https://www.youtube.com/channel/UCn2KHtlnvJNd3oRqH7tMjkg
email: emailtomohitsingh@gmail.com
Instagram: @mohit_was_here
"""
### Solution that appends directly to a list
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for x in range(1, n+1):
            if x % 3 == 0 and x % 5 == 0:
                out.append("FizzBuzz")
            elif x % 3 == 0:
                out.append("Fizz")
            elif x % 5 == 0:
                out.append("Buzz")
            else:
                out.append(str(x))
        return out

### Solution that uses a temporary string
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for x in range(1, n+1):
            temp = ''
            if x % 3 == 0:
                temp += 'Fizz'
            if x % 5 == 0:
                temp += 'Buzz'
            if (x % 5 != 0) and (x % 3 != 0):
                temp += str(x)
            out.append(temp)
        return out
