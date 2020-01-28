'''
Hackerrank.
Project Euler #1: Multiples of 3 and 5
    Task: Q. If we list all the natural numbers below 10 that are multiples of 3 or 5, we
    get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000. 
'''

'''
First-try iterative-based solution, that has bad optimization and takes a lot of time to compute.
sum = 0
for i in range(n):
    if((i % 3 ==0) or (i % 5 == 0)):
        sum = sum + i
print(sum)
'''
#!/bin/python3
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())        #Find sum below this n
    n = n - 1                       #Making border to ignore exactly value of n
    n3 = n // 3                     #Amount of numbers dividing by 3, 5
    n5 = n // 5
    n15 = n // 15                   #Amount of numbers dividing by 3 AND 5
    s3 = (3 * n3*(n3 + 1)) // 2     #Sum of the first n terms of AP
    s5 = (5 * n5*(n5 + 1)) // 2
    s15 = (15 * n15*(n15 + 1)) // 2 
    result = s3 + s5 - s15          #Substraction S15 because it contains common
    print(result)                   #numbers in S3 and S5
