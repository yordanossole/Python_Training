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

'''
