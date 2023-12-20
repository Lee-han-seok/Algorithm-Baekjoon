test_case = int(input())
cans = []
boxes = []
box_size = [[] for i in range(test_case)]

for i in range(test_case) :
    can, box = map(int, input().split(' '))
    cans.append(can)
    boxes.append(box)
    for j in range(box) :
        x, y = map(int, input().split(' '))
        box_size[i].append(x * y)

for i in range(test_case) :
    box_size[i].sort(reverse = True)

    remain_can = cans[i]
    for j in range(boxes[i]) :
        remain_can -= box_size[i][j]
        if remain_can <= 0 : 
            print(j+1)
            break
        else : 
            continue