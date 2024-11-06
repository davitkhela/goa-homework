# Create a string named quote with the following content: "To be or not to be, that is the question."
# Use the replace() function to replace the word "be" with "code". Store the result in a variable named modified_quote and print it.
quote =  "To {be} or not to {be}, that is the question."
modified_quote = "To {be} or not to {be}, that is the question.".format(be="code")
print(modified_quote)