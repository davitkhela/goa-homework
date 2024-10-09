#Create a list named temperatures that contains the following values representing daily temperatures: [72, 68, 75, 70, 78, 74, 71].
temperatures = [72, 68, 75, 70, 78, 74, 71]

# Calculate and print the highest temperature using the max() function.
print(max(temperatures))

# Calculate and print the lowest temperature using the min() function.
print(min(temperatures))

# Calculate and print the average temperature using the sum() function divided by the length of the list.
print(sum(temperatures)//len(temperatures))

# Use a list comprehension to create a new list named above_70 that contains only the temperatures above 70 degrees.
above_70 = [i for i in temperatures if i>70]

# Print the above_70 list.
print(above_70)