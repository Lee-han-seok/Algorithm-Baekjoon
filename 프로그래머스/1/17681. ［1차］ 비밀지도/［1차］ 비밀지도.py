def solution(n, arr1, arr2):
    # def fill_zero(num) :
    #     if len(num) == 1 :
    #         return '0000' + num
    #     elif len(num) == 2 :
    #         return '000' + num
    #     elif len(num) == 3 :
    #         return '00' + num
    #     elif len(num) == 4 :
    #         return '0' + num
    #     else :
    #         return num

    empty_square = [[0 for i in range(n)] for j in range(n)] 
    # 0으로 채워진 list (100,100)

    for i in range(n) :
        # format으로 b뒤의 숫자만 추출, zfill로 길이 통일 (부족한 만큼 앞단 0으로 fill)
        arr_1 = format(arr1[i],'b').zfill(n)
        arr_2 = format(arr2[i],'b').zfill(n)
        for j in range(n) :
            # 만약 둘 중 한개가 1이라면 # 반환, 아니면 공백 반환
            if arr_1[j] == '1' or arr_2[j] == '1' :
                empty_square[i][j] = '#'
            else :
                empty_square[i][j] = ' '
    # 각 list별로 떨어져있는 값들을 붙여준다.    
    for k in range(n) :
        tmp = ''
        for z in range(n) :
            tmp += empty_square[k][z]
        empty_square[k] = tmp

    answer = empty_square
    return answer