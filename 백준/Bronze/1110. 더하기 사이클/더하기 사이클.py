first_n = input()
trials = 1
previous_1, previous_2 = '', ''

if int(first_n) < 10 :
    previous_1, previous_2 = '0', first_n[0]
    first_n = previous_1 + previous_2
else : 
    previous_1, previous_2 = first_n[0], first_n[1]

#print(previous_1, previous_2)

while True :
    n = ''
    n = previous_2 + str(int(previous_1) + int(previous_2))[-1]
    previous_1, previous_2 = n[0], n[1]
    #print(n)
    if n == first_n :
        break
    else :
        trials+=1

print(trials)