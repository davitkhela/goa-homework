#asks the user to enter savings
savings = input("enter your savings: ")

#convert the user input into a float value and update the variable
savings = float(savings)

#savings grow after 1 year at a 5% annual interest rate
increase = 1.05
balance = savings * increase

# convert the balance into a string and update the variable
balance = str(balance)
message = "amount in 1 year: "
# concatenate the 2 strings to produce a message
amount_in_1_year = message + balance

# display the message
print(amount_in_1_year)
