# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d= defaultdict(list)
n,m= map(int,input().split())
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    value = input()
    if value in d:
        print(' '.join(map(str,d[value])))
    else:
        print(-1)
