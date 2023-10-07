from bisect import bisect_left, bisect_right

test_case = int(input())
for i in range(test_case) :  # test case만큼 반복 
    N_A, N_B = map(int, input().split()) 
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    B.sort() # bisect 사용을 위한 정렬
    results = [] # 결과 모아둘 list
    for x in range(len(A)) : # A리스트의 길이만큼 반복하면서
        results.append(bisect_left(B, A[x])) 
    # bisect_left를 사용해서 A의 각 원소가 B에 들어갈 때 왼쪽에서 출발해 가장 멀리 갈 수 있는 위치 반환 
    #(같은 숫자는 포함하면 안되기 때문에 right이 아닌 left 사용) 
    print(sum(results)) # 결과 list에 모여있는 값의 합을 출력하면 가능한 경우의 수의 합과 같다  
