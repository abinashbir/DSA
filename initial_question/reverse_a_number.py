number=78932

reverse=0
num = 0

# length=len(number)
# number=int(number)

# for i in range(length):

#     reverse=reverse+number%10 
#     number=number/10
while number > 0:
    num = number % 10
    reverse = reverse *10 + num
    number = number//10

print(reverse)
