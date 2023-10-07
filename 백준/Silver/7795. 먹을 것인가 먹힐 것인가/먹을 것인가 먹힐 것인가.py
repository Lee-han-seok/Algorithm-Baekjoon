from bisect import bisect_left, bisect_right

test_case = int(input())
for i in range(test_case) :   
    N_A, N_B = map(int, input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    B.sort()
    results = []
    for x in range(len(A)) :
        results.append(bisect_left(B, A[x]))
    print(sum(results))   