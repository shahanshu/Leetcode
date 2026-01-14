set1=set()
set1.update([1,2,3,4,5]) #duplcates are ignored
print(set1)

set2=set()
set2.update([1,4,5,6])
print(set2)
print(set1 & set2)
print(set1 ^ set2)
print(set1-set2)
print(set1 or set2 ) #duplicates are ignored in the sets 

set3=set(set2)
print(f'set3 : {set3}')
set2.add(88)
print(f'set2 : {set2}')
print(f'set3 : {set3}')