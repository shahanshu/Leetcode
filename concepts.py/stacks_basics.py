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
        
