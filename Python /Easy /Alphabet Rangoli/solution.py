import string
def print_rangoli(size):
    # your code goes here
    alpahbets = string.ascii_lowercase
    l=[]
    for i in range(size):
        alpa = '-'.join(alpahbets[i:size])
        l.append((alpa[::-1]+alpa[1:]).center(4*size-3,'-'))
    print('\n'.join(l[::-1]+l[1:]))

