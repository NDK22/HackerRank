# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
complex_number = complex(input())
print(abs(complex_number),phase(complex_number),sep='\n')
