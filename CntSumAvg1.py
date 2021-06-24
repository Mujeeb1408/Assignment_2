# Program to demonstrate Countintg ,Summing and average of numbers using loops
list1 = []
sum=0
avg=0
n=int(input('Enter the number of elements:'))
for i in range (0,n):
    num = int(input())
    sum = sum+num
    list1.append(num)
print('Counting = ',len(list1))
print('Sum of numbers: ',sum)
print('Average of numbers:',(sum/len(list1)))