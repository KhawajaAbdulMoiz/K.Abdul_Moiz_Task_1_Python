
# Q1) Declare two variables, num1 and num2, with any integer values:
num1 = 18
num2 = 23

# Calculating their sum:
sum_result = num1 + num2

# Printing the result:
print(f"Sum of", num1, "and", num2, "is:", sum_result)

# End of Question_1

# Q2) Create a variable called message and give it a string value:
message = "HELLO"

# Append the string " World!" to it: 
message += " WORLD!"

# Printing the updated message:
print(message)

# End of Question_2

# Q3) Declare a variable, is_python_fun, and assign it a boolean value:
is_python_fun = True

# Printing a statement based on whether Python is considered fun:
if is_python_fun:
    print("Python is fun!")
else:
    print("Python is not fun.")

# End of Question_3

# Q4) Create a list called fruits with at least three different fruit names:
fruits = ['Papaya', 'Orange', 'Pear']

# Printing the list:
print("Fruits:", fruits)

# Adding a new fruit:
fruits.append('Mango')

# Printing the updated list:
print("Updated list of Fruits:", fruits)

# End of Question_4

# Q5) Declare a variable called price with a floating-point value:
price = 84.18

# Converting it to an integer:  
converted_price = int(price)

# Printing both original and converted values:
print("Original Price:", price)
print("Converted Price:", converted_price)

# End of Question_5

# Q6) Create a dictionary named student_info with keys for 'name', 'age', and 'grade':
student_info = {'Name': 'Moiz', 'Age': 18, 'Grade': 'A-ONE'}

# Printing the dictionary:
print("Student Information:", student_info)

# End of Question_6

# Q7) Write a program that takes user input for their age: 
user_age = int(input("Enter your age: "))

#  Printing a message addressing their age group:
if user_age < 12:
    print("Child")
elif 12 <= user_age < 18:
    print("Teenager")
else:
    print("Adult")

# End of Question_7

# Q8) Create a complex number variable, comp_num, with real and imaginary parts:
comp_num = 7 + 9j

# Printing both parts separately:
print("Real part:", comp_num.real)
print("Imaginary part:", comp_num.imag)

# End of Question_8

# Q9) Combine two strings using concatenation:
string1 = "Hello"
string2 = "Sir"
combined_string = string1 + " " + string2

# Using string interpolation to include the length of the resulting string in a print statement:
print("Combined String:", combined_string,",", "Length:", len(combined_string))

# End of Question_9

# Q10) Create a tuple named days_of_week with the names of the days:
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# Accessing and printing the third day of the week:
print("Third day of the week:", days_of_week[2])

# End of Question_10

