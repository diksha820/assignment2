#function in python
#1. Write a function to check whether a number is positive, negative, or zero. 
"""
def check_number(num):
    if num>0:
        print("positive ")
    elif num<0:
        print("negative ")
    else:
        ("zero")
check_number(98)


#2.	Write a function to check whether a number is even or odd. 
def check_number(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
check_number(7)


#3.	Write a function that accepts two numbers and returns the greater number. 
def number(a,b):
    if a>b:
        return a
    else:
        return b
number(greater(4,8))   


#4.	Write a function to check whether a person is eligible to vote (age ≥ 18). 
def vote(age):
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")
vote(99)


#5.	Write a function to check whether a number is divisible by 5. 
def check_number(num):
    if num%5==0:
        print("divided by 5")
    else:
        print("not divided by 5")
check_number(67)


#6.	Write a function to check whether a given year is a leap year or not. 
def year(num):
    if num%4==0:
        print("leap year")
    else:
        print("not a leap year")
year(2027)

#7.	Write a function to check whether a character is a vowel or a consonant. 
def check_character(ch):
    if ch.lower() in"aeiou":
        print("vowel")
    else:
        print("constant")
check_character("d")

#8.	Write a function to find the largest among three numbers. 
def largest_num(a,b,c):
    if a>=b and a>=c:
        print(a)
    elif b>=c:
        print(b)
    else:
        print(c)
largest_num(23,65,34)

#9.	Write a function to calculate the sum of numbers from 1 to 100. 
def sum():
    total = 0
    for i in range(1,101):
        total += i
    return total
print(sum())


#10. Write a function that prints the multiplication table of a given number. 
def table(num):
    for i in range(1,11):
        print(num,"x",i,"=",num*i)
table(88)


#11. Write a function to calculate and return the square of a number. 
def square(num):
    return num*num
print(square(8))


#12. Write a function to calculate the factorial of a number using a loop. 
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact *= i
    return fact
print(fact(7))

#13. Write a function to check whether a number is prime. 
def prime_num(num):
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            return
    print("prime")
prime_num(8)

#14. Write a function to calculate the sum of digits of a number. 
def sum(num):
    total =0
    while num>=0:
        total +=num %10
        num//=10
    return total
print(sum(2736))


#15. Write a function that accepts a number n and returns the sum of all numbers from 1 to n.
def sum(n):
    total =0
    for i in range (1,n+1):
        return total
    print(total)
sum(45)
"""



#list in python
#1.create a list of 10 numbers and print all elements
list=[0,9,8,7,6,5,4,3,2,1]
print(list)

