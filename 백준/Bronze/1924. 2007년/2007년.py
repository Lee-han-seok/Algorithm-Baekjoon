year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
month, day = map(int, input().split())

num = 0
for i in range(month - 1) :
    num += year[i]

num = (num + day) % 7

print(week[num])