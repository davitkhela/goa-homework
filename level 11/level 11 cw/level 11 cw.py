# take steps and minutes as inputs
steps = int(input("enter your steps:"))
active_minutes = int(input("enter your minutes:"))

# store the result of operations in a variable
goal_achieved = (10000<=steps or 30<=active_minutes)

# display the result on the screen
print(goal_achieved)