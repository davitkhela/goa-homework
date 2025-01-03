def even_numbers(arr,n):
    number = []
    for i in arr:
        if i % 2 == 0:
            number.append(i)
    return number[-n:]



def sum_of_n(n):
    if n >= 0:
        return [sum(range(arr + 1)) for arr in range(n + 1)]
    else:
        return [sum(range(arr + 1)) for arr in range(0, abs(n) + 1)][::-1]
    

print(sum_of_n(-5))