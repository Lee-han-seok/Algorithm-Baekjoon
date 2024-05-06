while True :
    ans = int(input())
    if ans != -1 :
        tmp = []
        for i in range(1, ans) :
            if ans % i == 0 :
                tmp.append(i)
        if sum(tmp) == ans :
            results = [ans, '=', ]
            for i in tmp :
                results.append(i)
                results.append('+')
            print(*results[:-1])
        else :
            print(f'{ans} is NOT perfect.')
    else :
        break