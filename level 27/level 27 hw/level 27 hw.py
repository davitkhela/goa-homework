# Create a string named template with the following content: "Hello, {name}. Welcome to {place}."Use the format() function to replace {name} with "Alice" and {place} with "Wonderland". Store the result in a variable named formatted_string and print it.
name = 'Alice'
place = 'Wonderland'
template = ("Hello, {name}. Welcome to {place}.")
formatted_string = ("Hello, {name}. Welcome to {place}.").format(name=name,place=place)
print(formatted_string)