# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
To_permute , length_of_permutation = input().split()
print( *[''.join(permutes) for permutes in permutations(sorted(To_permute),int(length_of_permutation))],sep='\n')

