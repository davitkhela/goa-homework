# შექმენი ფუნქცია, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს სიის საშუალო რიცხვს.

def numbers(n):
    if len(n) == 0:
        return 'the number is 0'
    else:
        return sum(n)//len(n)