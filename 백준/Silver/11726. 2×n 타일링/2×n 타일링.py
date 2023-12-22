num = int(input())

# 점화식 : a(n) = a(n-1) + a(n-2)

result_list = [1, 2]
for i in range(2, num + 1) :
    result_list.append((result_list[i - 2] + result_list[i-1]) % 10007)

print(result_list[num-1])