# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    N = input()
    integer_list=map(int,input().split())
    i=tuple(integer_list)
    print(hash(i))
#
