def main (verb, noun):
    return verb + noun


def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def mod(a, b):
    return a%b

def exponent(a, b):
    return a**b

def subt(a, b):
    return a-b


def simple_multiplication(number) :
    if number % 2 == 0:
        return number*8
    else:
        return number*9
    

def is_even(n): 
    if n % 2 == 0:
        return True
    else:
        return False
    


def solution(string):
    return string[::-1]


def boolean_to_string(b):
    return str(b)


def greet(name):
    return  f"Hello, {name} how are you doing today?"

def paperwork(n, m):
    if n>0 and m>0:
        return n*m
    else:
        return 0
    
