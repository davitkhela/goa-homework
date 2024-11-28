# შექმენი პროგრამა, რომელიც იფუნქციონირებს შემდეგნაირად: მომხმარებლის შეყვანილი რიცხვი იქნება დადებითი, უარყოფითი, ან ნულოვანი, და შესაბამისი შეტყობინება უნდა გამოიტანოს.


n = float(input('enter a number:'))


if n > 0:
    print('positive')
elif n == 0:
    print('the number is zero')
else:
    print("negative")