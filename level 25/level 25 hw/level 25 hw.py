def paperwork(n, m):
    if n < 0 or m < 0:
       return 0
    return n * m


def quarter_of(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4
    else:
        return "Invalid month"
    

def bool_to_word(boolean):
     return "Yes" if boolean else "No"


def greet(name):
    return "Hello, " + name + " how are you doing today?"