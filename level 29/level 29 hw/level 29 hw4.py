# შექმენი ფუნქცია, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს ორ ცალკე სიას – ერთში იქნებიან ლუწი რიცხვები, ხოლო მეორეში კენტი რიცხვები.


def separate_even_odd(numbers):
    even_numbers = [] 
    odd_numbers = [] 
    for number in numbers: 
        if number % 2 == 0: 
            even_numbers.append(number) 
        else: 
            odd_numbers.append(number) 
    return even_numbers, odd_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
even, odd = separate_even_odd(numbers)

print(even)
print(odd)