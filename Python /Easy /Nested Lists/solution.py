if __name__ == '__main__':
    results=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        results.append([name,score])
    second_lowest_score = sorted(set(score for name, score in results))[1]
    names_of_2nd_lowest_score = sorted(name for name, score in results if score == second_lowest_score)
    [print(name) for name in names_of_2nd_lowest_score]
