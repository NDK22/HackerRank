def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        seen= set()
        result = [char for char in string[i:i+k] if char not in seen and not  seen.add(char)]
        print(''.join(result))
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
