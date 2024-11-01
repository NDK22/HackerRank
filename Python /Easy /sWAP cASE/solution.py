def swap_case(s):
    # result=''
    # for char in s:
    #     if char.isupper():
    #         char=char.lower()
    #         result+=char
    #     else:
    #         char=char.upper()
    #         result+=char
    s=s.swapcase()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
