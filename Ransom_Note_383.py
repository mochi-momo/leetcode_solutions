### Solve with Counter Method (Dictionary)
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        mag = Counter(magazine)
    
        for key in ran:
            if ran[key] > mag[key]:
                return False
        
        return True

### Solve with list
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)
        for char in ransomNote:
            if char in mag:
                mag.remove(char)
            else:
                return False
        return True