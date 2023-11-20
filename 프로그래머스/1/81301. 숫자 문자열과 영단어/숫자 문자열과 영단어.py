def solution(s):
    
    nums = ['0','1','2','3','4','5','6','7','8','9']
    words = ['zero', 'one', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    words_nums = dict(zip(words, nums))
    
    for word, num in words_nums.items() :
        if word in s :
            s = s.replace(word, num)
        else :
            continue
            
    answer = int(s)
    return answer