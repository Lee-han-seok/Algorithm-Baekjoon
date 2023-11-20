from collections import Counter

num, length = map(int, input().split(' '))

dna_lists = [[] for _ in range(length)]  # 빈 리스트 생성

# 입력받은 후, 각 자리수로 분리하여 저장한다.
for _ in range(num):
    dna = input()
    for j in range(length):
        dna_lists[j].append(dna[j])

result_str = ''  # 결과 문자열을 반환받는다.
diff = 0  # 각 자리에서 다른 DNA가 나타난 횟수 초기화

for k in range(len(dna_lists)):
    tmp = Counter(dna_lists[k]).most_common()  # Counter를 이용해 최빈값 찾기
    if len(tmp) != 1:  # 최빈값이 1개가 아니라면,
        result_str += min([i[0] for i in tmp if i[1]==tmp[0][1]])
    else:
        result_str += tmp[0][0]  # 최빈값이 1개면, 해당 값을 출력 (모두 같은 값임)

for k in range(num):
    for j in range(length):
        if result_str[j] != dna_lists[j][k]:
            diff += 1

print(result_str, diff, sep='\n')