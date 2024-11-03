# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    sizes = input().split()
    length,wide=int(sizes[0]),int(sizes[1])
    pattern=".|."
    mid=(length//2+1)
    for i in range(1,length+1):
        if i < mid:
            print((pattern*(i*2-1)).center(wide,'-'))
        elif i == mid:
            print('WELCOME'.center(wide,'-'))
        else:
            print((pattern*((length-i+1)*2-1)).center(wide,'-'))
