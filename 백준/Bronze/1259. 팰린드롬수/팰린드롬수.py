while True :
    a = input()
    if a == str(0) :
        break
    if a == a[::-1]:
        print('yes')
    else : 
        print('no')