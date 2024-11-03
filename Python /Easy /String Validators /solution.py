if __name__ == '__main__':
    s = input()
    # alphanumeric=False
    # alphabetical=False
    # digits=False
    # lowercase=False
    # uppercase=False
    # for char in s:
    #     if char.isalnum():
    #         alphanumeric=True
    #     if char.isalpha():
    #         alphabetical=True
    #     if char.isdigit():
    #         digits=True
    #     if char.islower():
    #         lowercase=True
    #     if char.isupper():
    #         uppercase=True
    # print(alphanumeric,alphabetical,digits,lowercase,uppercase, sep='\n')
            
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))
