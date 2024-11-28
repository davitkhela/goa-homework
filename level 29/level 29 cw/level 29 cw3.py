def search(text,word):
    if word in text:
        return 'word found'
    else:
        return 'word not found'

text = input('enter your text: ')
word = input('enter your word: ')

print(search(text,word))