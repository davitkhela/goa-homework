"""
    შექმენი ფუნქცია, რომელიც მიიღებს ტექსტს და გამოითვლის, რამდენი სიტყვაა ამ ტექსტში.
"""


def word_len_count(text_to_use):
    split_text = text_to_use.split()
    return len(split_text)

text_to_use = input("")
print(word_len_count(text_to_use))