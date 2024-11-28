# შექმენი პროგრამა, რომელიც მიიღებს მომხმარებლის ასაკს და დააბრუნებს შეტყობინებას იმის მიხედვით, თუ რომელ ასაკობრივ კატეგორიაშია მომხმარებელი.

def age_category(user_age):
    if 0 < user_age < 13:
        return 'child'
    if 13 <= user_age < 18:
        return 'teenager'
    elif 18 <= user_age <= 140:
        return 'adult'
    else:
        return 'alien'
    
user_age = float(input('enter your age:'))

print(age_category(user_age))