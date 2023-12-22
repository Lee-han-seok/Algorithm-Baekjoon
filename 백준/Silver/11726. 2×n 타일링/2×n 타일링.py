num = int(input())

result_list = [1, 2]
for i in range(2, 1000) :
    result_list.append((result_list[i - 2] + result_list[i-1]) % 10007)

print(result_list[num-1])