string='anshukumarshah'

from collections import defaultdict

count=defaultdict(int)

for i in string:
    count[i]+=1
for kripa,vale in string:
    if count[vale]==1:
     print(kripa)
    else:
        print('-1')

