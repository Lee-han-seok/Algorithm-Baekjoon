from bisect import bisect_left, bisect_right

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

for m in M_list :
    print(bisect_right(N_list, m) - bisect_left(N_list, m))