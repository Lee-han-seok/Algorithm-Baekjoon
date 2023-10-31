from collections import Counter

strings = input().strip()

strings = strings.upper()

counter_strings = Counter(strings).most_common()

if len(counter_strings) == 1 :
    print(counter_strings[0][0])
else :
    if counter_strings[0][1] == counter_strings[1][1] :
        print('?')
    else :
        print(counter_strings[0][0])