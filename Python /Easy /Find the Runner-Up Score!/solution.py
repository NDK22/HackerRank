if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up_score= sorted(set(arr),reverse=True)[1]
    print(runner_up_score)
