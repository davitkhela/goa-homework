"""
    შექმენი ფუნქცია, რომელიც მიიღებს ტექსტს და გამოითვლის, რამდენი სიტყვაა ამ ტექსტში.
"""

def count(text):
    return len(text)

text = input('enter your text here: ')

print(count(text))