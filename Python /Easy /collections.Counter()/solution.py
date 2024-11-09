# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
number_of_shoes = input()
number_of_sizes_available = Counter(map(int,input().split()))
number_of_customers = int(input())
earned=0
for i in range(number_of_customers):
    size , price = map(int,input().split())
    if number_of_sizes_available[size]>0:
        earned += price
        number_of_sizes_available[size] -= 1
print(earned)
