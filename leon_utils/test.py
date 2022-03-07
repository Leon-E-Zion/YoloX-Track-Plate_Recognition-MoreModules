# 字母转数字
J=11
Q=12
K=13
A=14
T=15
S=16
def to_num(num):
    if num =='J':
        return 11
    elif num =='Q':
        return 12
    elif num =='K':
        return 13
    elif num =='A':
        return 14
    elif num =='T':
        return 15
    elif num =='S':
        return 16
    else:
        return int(num)
# print(to_num(12))
def to_int(num):
    num_ = 0
    for i,a in enumerate(num):
        a = to_num(a)
        print(a)
        # 越靠前越重要
        num_ += 10**((len(num)-i)*int(a))
    return num_
to_int('SSSS')

def get_big(num_0,num_1):
    if num_0>= num_1:
        print(num_0)
    else:
        print(num_1)
get_big('SSS','HHHH')