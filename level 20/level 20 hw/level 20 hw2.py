# not და in keyword-ების გამოყენება სიაში

# შექმენი სია სახელწოდებით fruits, რომელიც შეიცავს რამდენიმე ხილის დასახელებას.
fruits = ['mango', 'apricot', 'kiwi',]

# შეამოწმე, არის თუ არა apple სიის ნაწილი. თუ არაა, დაამატე იგი.
if 'apple' not in fruits:
    fruits = fruits + ['apple']

# გამოყენებით not in, დარწმუნდი რომ banana არ არის სიაში და დაბეჭდე შესაბამისი შეტყობინება.
if 'banana' not in fruits:
    print('banana is not in the list')


print(fruits)

