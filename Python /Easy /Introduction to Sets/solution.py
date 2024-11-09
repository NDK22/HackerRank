def average(array):
    # your code goes here
    array_set=set(array)
    avg = sum(array_set)/len(array_set)
    return round(avg,3)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
