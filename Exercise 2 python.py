# Question 1: Arithmetic and Assignment Operators
x = 10
y = 5
# TODO: Add 3 to x using the += operator
x +=3
# TODO: Multiply y by 2 using the *= operator
y *=2
# TODO: Divide x by y and store the result in a variable called 'result
result= x/y
# TODO: Print the value of 'result'
print(result)

#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a=9
b=3
c=6 
# TODO: Create a condition that checks if a is greater than b
print(a > 3)
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
modulus=b % 2 
modulus= b == 0 
# TODO: Create a condition that checks if c is less than or equal to a
print(c <= a)
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition=(a>b) or (modulus and c<=a) 
# TODO: Print the value of 'final_condition'
print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score=int(input("what is the test score?"))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if score >=90 : 
   print("A")
elif score >=80 : 
   print("B")
elif score >=70 :
   print("C")
elif score >=60 :
   print("D")
else:   
   print("F")
# TODO: Print the grade for the given score
print(score)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1=int(input("insert a number"))
num2=int(input("insert another number"))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation=int(input("+,-,*,/"))
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
result=0
if operation=="+": 
   result = num1 + num2
   print(result)

elif operation=="-":
   print(result)
elif operation=="*":
   print(result)
elif operation=="/":
   print(result)
else:
   print(result)
# TODO: Handle the case of division by zero
operation=num1=num2=0 

# TODO: Print the result of the operation
print(result)