anshu=[]

anshu.append('A')
anshu.append(23)
print(f"stack: {anshu}")
anshu.pop()
print(f"stack : {anshu}")

print(not bool (anshu))


""""
using class 
"""
class anshu:
    def __init__(self):
        self.anshu=[]
    def insert(self,element: int) -> int:
        self.anshu.append(element)
        
'''
stack.append(x) where x=any
stack.pop() -> pops the last inserted element
stack[-1] gives the last emlemet as like in the list[:b]
'''


"""
Is there nesting/matching? ──Yes──→ Stack (e.g., parentheses)
        │
        No
        ↓
Looking for "next greater/smaller"? ──Yes──→ Monotonic Stack
        │
        No
        ↓
Building optimal sequence by removing bad prefixes? ──Yes──→ Greedy + Stack
        │
        No
        ↓
Simulating DFS or backtracking locally? ──Yes──→ Stack as recursion substitute
        │
        No
        ↓
→ Probably not a stack problem.
"""