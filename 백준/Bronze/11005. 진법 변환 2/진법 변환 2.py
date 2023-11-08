num, div = input().split()
refer = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''

while num :
    result += refer[int(num) % int(div)]
    num, _ = divmod(int(num), int(div))

print(result[::-1])