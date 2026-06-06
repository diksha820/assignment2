#1. Create a list of 10 numbers and print all the elements.

number=[2,1,3,6,5,7,8,9,0,4]
for i in number:
    print(i)


#2.	Write a program to find the largest element in a list.
number=[32,56,7,34,98,65]
largest=number[0]
for i in number:
    if i>largest:
        largest=i
print("larest number",largest)


#3.	Write a program to find the smallest element in a list. 
numbers=[34,5,2,45,57,25,54]
smallest = numbers[0]
for i in numbers:
    if i<smallest:
        smallest=i
print("smallest number",smallest)


#4.	Write a program to calculate the sum of all elements in a list. 
number=[4,67,23,76,23,56,34,56,3487,3467]
total=0
for i in number:
    total=total+i
print("sum",total)


#5.	Write a program to calculate the average of all elements in a list. 
number=[23,4,45,32,67,32,65,74,32,65]
total=0
for i in number:
    total=total+i
average=total/len(number)
print("average=",average)


#6.	Write a program to count how many even numbers are present in a list. 
number=[5,3,2,5,4,2,1,4,1]
count=0
for i in number:
    if i in number:
        count+=1
print("even number count=",count)


#7.	Write a program to create a new list containing only the odd numbers from an existing list. 
number=[10,15,20,25,30,35]
odd_number=[]
for i in number:
    if i%2!=0:
        odd_number.append(i)
print("odd number:",odd_number)


#8.	Write a program to find whether a given element exists in a list. 
number=[10,20,30,40,50]
element=90
if element in number:
    print("element found")
else:
    print("element not found")

#9.	Write a program to reverse a list without using built-in reverse functions.
number=[45,36,47,34,95,54,45]
reverse=[]
for i in range(len(number)-1,-1,-1):
    reverse.append(number[i])
print("reverse list",reverse)

#10.Write a program to findsecond largest elemnet in a list
number=[10,25,5,40,15]
number.sort()
print("second largest element :",number[-2])