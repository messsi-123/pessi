def prime_ factors(x):
i=2
while i <= x:
if x % i == 0 :
print(i, end=' ')
while x % i == 0:
x = x // i
i += 1
num =int(input("Enter a number: "))
prime_factors (num)