### Suboptimal Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True
        return False

### Better Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False

### One Line Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]