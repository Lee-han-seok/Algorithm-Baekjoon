N = int(input())
x_list = []
y_list = []
for n in range(N) :
    x, y = input().split()
    x_list.append(int(x))
    y_list.append(int(y))
for i in range(len(x_list)) :
    count = 1
    for j in range(len(y_list)) :
        if (x_list[i] < x_list[j]) & (y_list[i] < y_list[j]) :
            count += 1
    print(count, end = ' ')