#Calculate Factorial
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24"""

num = int(input("Enter the number you want to calculate the factorial : "))
factorial = 1
for i in range(1, num + 1):
 factorial = factorial * i
print("The factorial of" ,num, "is", factorial)