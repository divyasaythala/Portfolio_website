from itertools import permutations
arr=[1,2,3]
s=permutations(arr)
print([list(p) for p in s])

from itertools import combinations
n=4
k=2
for i in range(1,n):
    com=combinations(i,k)
    print([list(p) for p in com])
