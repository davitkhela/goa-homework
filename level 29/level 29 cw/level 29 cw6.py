"""
 შექმენი პროგრამა, რომელიც მიიღებს მომხმარებლის ასაკს და დააბრუნებს შეტყობინებას იმის მიხედვით, თუ რომელ ასაკობრივ კატეგორიაშია მომხმარებელი.
"""
def age_category(age):
    if 0 < age < 13:
        return 'child'
    if 13 <= age < 18:
        return 'teenager'
    else:
        return 'adult'
    
age = int(input('enter your age:'))

print(age_category(age))