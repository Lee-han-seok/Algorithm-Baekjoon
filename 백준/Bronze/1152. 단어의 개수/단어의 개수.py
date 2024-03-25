answer = input()
if answer == ' ' :
    print(0)
else :
    print(len(answer.strip().split(' ')))