"""
1. Write a program to read two integers from STDIN and print five lines where:
A. The first line contains the sum of the two numbers.
B. The second line contains the difference of the two numbers (first - second).
C. The third line contains the product of the two numbers.
D. The output of an integer division (first divided by second).
E. The output of the division (first divided by second).
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

nSum = num1 + num2
nDifferece = num1 - num2
nProduct = num1 * num2
nIntDivision = num1 // num2
nDivision = num1 / num2
print("Their sum: ", nSum)
print("Their difference: ", nDifferece)
print("Their product: ", nProduct)
print("Their floor division: ", nIntDivision)
print("Their division: ", nDivision)

"""
2. Create a program to take the details of an employee (Name, Age, Position, and Salary)
from STDIN and print the four lines each containing one detail per line of the employee.
"""
name = input("Enter employee name: ")
age = int(input("Enter employee age: "))
position = input("Enter employee position: ")
salary = float(input("Enter employee salary: "))

print("Name: ", name, "\nAge: ", age, "\nPosition: ", position, "\nSalary: ", salary)

"""
3. Create a program in which you will have two variables. These variables shall be assigned
different types of values (integer, float, complex, string) at different times. Print the
values and the types of the variables (one in each line) each time you assign a new value.
"""

num = 10
print(num)
print(type(num))

name = "Yordanos"
print(name)
print(type(name))


"""
4. Write a program to remove characters from a string starting from zero up to n and
return a new string.
"""

"""
5. Given two integer numbers return their product only if the product is equal to or lower
than 1000, else return their sum.
"""


def result(num1, num2):
    product = num1 * num2
    SUM = num1 + num2
    if product <= 1000:
        return print("Product: ", product)
    else:
        return print("Sum: ", SUM)
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result(num1, num2)


"""
6. Given an integer, n, perform the following conditional actions:

 If n is odd, print Weird
 If n is even and in the inclusive range of 2 to 5, print Not Weird
 If n is even and in the inclusive range of 6 to 20, print Weird
 If n is even and greater than 20, print Not Weird.
"""
def checkEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
        
def checkWeird(n):
    if checkEven(n):
        print("Weird")
    elif checkEven(n) and n>=2 and n<=5:
        print("Not weird")
    elif checkEven(n) and n>=6 and n<=20:
        print("Weird")
    elif checkEven(n) and n>20:
        print("Not weird")
    else:
        print("Odd")

n = int(input("Enter a number: "))
checkWeird(n)

"""
7. Write a program that takes three numeric values from STDIN and checks if these three
numeric values can be valid sides of a triangle.
"""

"""
Triangle Inequality Theorem: This theorem states that the sum of any two sides of a 
triangle must be greater than the third side. If this condition holds true for all 
three combinations of side lengths, then you have a valid triangle. You can express 
the theorem as inequalities:
(a + b > c)
(a + c > b)
(b + c > a)
"""
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print(f"The three values{a,b,c} are valid sides of a triangle.")
else:
    print(f"The three values{a,b,c} are invalid sides.")


"""
8. Write a program that takes a numeric score of a student out of 100 from STDIN and
assigns a letter grade for the given score.
"""

name = input("Enter your name: ")
score = float(input("Enter your score: "))
grade = None
if score >= 90:
    grade = 'A+'
elif score >= 83:
    grade = 'A'
elif score >= 80:
    grade = 'A-'
elif score >= 75:
    grade = 'B+'
elif score >=68:
    grade = 'B'
elif score >= 65:
    grade = 'B-'
elif score >= 60:
    grade = 'C+'
elif score >= 50:
    grade = 'C'
elif score >= 45:
    grade = 'C-'
elif score >= 40:
    grade = 'D'
else:
    grade = 'F'

print(name, "Your grade is", grade)

"""
9. Write a program to read two strings from STDIN and print the two lines where:
A. The first line contains the concatenation of the two strings (first followed by second).
B. The second line contains the concatenation of the first half of the first, the first half of
the second, the second half of the first, the second half of the second.
"""

inpStr1 = input("First input: ")
inpStr2 = input("Second input: ")
size1 = len(inpStr1)
size2 = len(inpStr2)

half1 = size1//2
half2 = size2//2

last1 = size1 - 1
last2 = size2 - 1
print(inpStr1 + inpStr2)
print(inpStr1[0:half1] + inpStr2[0: half2] + inpStr1[half1: size1] + inpStr2[half2: size2])
