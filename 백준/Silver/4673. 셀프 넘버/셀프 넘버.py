self_numbers = []
array = list(range(1,10000))

for num in array :
    fixed_len = len(str(num))
    tmp_num = num
    for j in range(fixed_len) :
        tmp_num += int(str(num)[j])
    self_numbers.append(tmp_num)

array_to_set = sorted(list(set(array) - set(self_numbers)))
for array in array_to_set :
    print(array)