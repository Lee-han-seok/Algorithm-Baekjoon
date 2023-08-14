T = int(input())

for i in range(T) :
    floors = int(input())
    hos = int(input())
    zero_floor = list(range(1,hos+1))

    for floor in range(1, floors+1) :
        for ho in range(1, hos) :
            zero_floor[ho] += zero_floor[ho-1]
    print(zero_floor[-1])