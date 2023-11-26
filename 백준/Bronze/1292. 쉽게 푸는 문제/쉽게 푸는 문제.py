tmp_list = []
front, back = map(int, input().split())
for i in range(1000) :
    tmp_list += ([i] * i) 

print(sum(tmp_list[front - 1 : back]))