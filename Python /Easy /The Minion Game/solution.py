def minion_game(string):
    # your code goes here
    vowels={'A','E','I','O','U'}
    stuart_score=0
    kevin_score=0
    for i in range(len(string)):
        if string[i] not in vowels:
            stuart_score+=(len(string)-i)
        else:
            kevin_score+=(len(string)-i)
    if stuart_score > kevin_score:
        print('Stuart',stuart_score)
    elif stuart_score < kevin_score:
        print('Kevin',kevin_score)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
