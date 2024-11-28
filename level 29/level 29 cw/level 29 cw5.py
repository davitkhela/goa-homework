"""
    შექმენი პროგრამა, რომელიც იფუნქციონირებს შემდეგნაირად: მომხმარებლის შეყვანილი რიცხვი იქნება დადებითი, უარყოფითი, ან ნულოვანი, და შესაბამისი შეტყობინება უნდა გამოიტანოს.
"""

def number(n):
    if n > 0:
        return 'positive'
    if n == 0:
        return 'neither positive or negative, it is zero'
    if n < 0:
        return 'negative'



n = float(input("enter a number: "))

print(number(n))