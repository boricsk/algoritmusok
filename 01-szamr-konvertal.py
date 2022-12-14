
def konvert(num,base):
    chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D']
    result = []
    while num != 0:
        result += chars[(num % base)]
        num = num // base
    
    return ''.join(result[::-1])

print(konvert(213,2))