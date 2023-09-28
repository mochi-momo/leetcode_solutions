"""
LinkedIn: https://www.linkedin.com/in/mochi-momo/
github: https://github.com/mochi-momo
email: emailtomohitsingh@gmail.com
"""
### Simple Solution
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp = []
        for row, soldiers in enumerate(mat):
            temp.append((sum(soldiers), row))
        temp.sort()
        
        out = []
        for val in temp[:k]:
            out.append(val[1])
        return out

### Solution with a more complex but effecient return
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp=[]
        for row, soldiers in enumerate(mat):
            temp.append((sum(soldiers),row))      
        temp.sort()
       
        return [val[1] for val in temp[:k]]  
