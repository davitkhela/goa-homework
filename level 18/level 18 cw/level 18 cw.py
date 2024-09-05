# ააგეთ პროგრამა, რომელიც მოსთხოვს მომხმარებელს, რომ შეიყვანეს რიცხვი 1 - 100 მდე. პროგრამის დანიშნულება არის ის, რომ გამოიცნოს მომხმარებლის მიერ შემოტანილი რიცხვი, იმდენჯერ მიეცეს გამოცნობის შესაძლებლობა სანამ საბოლოოდ არ გამოიცნობს.

import random

def guess_number():
    while input("Think of a number between 1 and 100, and I will try to guess it. Ready? (yes/no): ").lower() != 'yes':
        pass
    
    while True:
        guess = random.randint(1, 100)
        if input(f"Is {guess} your number? (yes/no): ").lower() == 'yes':
            break
    
    print(f"Yay! I guessed your number, {guess}, correctly!")

guess_number()
