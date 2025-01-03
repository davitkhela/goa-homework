def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i += 1
    return res


def grow(arr):
    res = 1
    for i in arr:
        res*=i
    return res


def fake_bin(x):
    res=''
    for i in x:
        if int(i) < 5:
            res += '0'
        else:
            res += '1'
    return res

