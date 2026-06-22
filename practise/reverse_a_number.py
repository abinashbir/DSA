number=78932

reverse=0
num = 0

while number > 0:
    num = number % 10
    reverse = reverse *10 + num
    number = number//10

print(reverse)
