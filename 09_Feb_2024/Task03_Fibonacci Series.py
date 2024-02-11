#Fibonaci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13

n = int(input("Enter the Number : "))
num1 = 0
num2 = 1
for i in range(0,n):
    print(num1, end = " ")
    num3 = num1+num2
    num1 = num2
    num2 = num3

