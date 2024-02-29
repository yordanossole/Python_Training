Exercises on Loops
#1. Print First 10 natural numbers using while loop.
i = 1
while i<11:
    print(i)
    i += 1
#2. Write a program to print the following number pattern using a loop.
#i.e right side right angle triangle
for i in range(1, 6):
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
"""3. Write a program to accept a number from a user and calculate the
sum of all numbers from 1 to a given number, n."""
x = int(input("Enter a number to calculate the first integers upto you entered: "))
result = 0
for i in range(1, x+1):
    result += i
print("result: ", result)
'''
4. Write a program to print multiplication table (up to 10) of a given
number, n. Constraints 1≤ n ≤ 10
'''
n = 10#int(input("Enter a number upto 10 to produce a multiplication table: "))
print("Multiplication table upto ", n)
for i in range(1, n+1):
    for j in range(1, n+1):
        result = i * j
        print(result, end = '\t')
    print()

'''
5. Write a program to count the total number of digits in a number 
using a while loop
'''
num = int(input("Enter a number to count the digit: "))

counter = 0
while num != 0:
    num //= 10
    counter += 1

print("The number of the digit is: ", counter)

'''
6. Write a program to use for loop to print the following reverse 
number pattern.
'''
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = ' ')
    print()

'''
7. Display numbers from -10 to -1 using for loop.
'''
for i in range(-10, 0):
    print(i, end = ' ')

'''
8. Use else block to display a message “Done” after successful execution 
of for loop
'''
for i in range(0, 5):
    flag = True
if flag == False:
    print("Not done")
else:
    print('Done')

'''
9. Write a program to display all prime numbers within a range. Take 
the range lower and upper bounds from the user as an input. 
'''
for i in range(num1, num2):
    counter = 0
    for j in range(1, i+1):
        if i%j == 0:
            counter += 1
    if counter == 2:
        print(i, end = ' ')
'''
Exercises on Functions
10. Write a program to create a function that takes two arguments, name 
and age, and print their value.
'''
def nameAge(name, age):
    print("Name: ", name)
    print("Age: ", age)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

nameAge(name, age)

'''

'''

