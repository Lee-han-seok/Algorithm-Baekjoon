numbers = [1,2,3,4,5,6,7,8,9]
alphas = ['ABC','DEF','GHI','JKL','MNO', 'PQRS','TUV','WXYZ']

dic = list(zip(numbers, alphas))

sangun = input()
alpha_to_num = ''
for i in range(len(sangun)) :
    for j in range(len(dic)) :
        if sangun[i] in dic[j][1] :
            alpha_to_num += str(dic[j][0])
        else :
            pass

times = len(alpha_to_num)
for i in range(len(alpha_to_num)):
    times += int(alpha_to_num[i]) + 1

print(times) 