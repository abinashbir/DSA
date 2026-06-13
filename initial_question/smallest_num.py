numbers=[2,5,1,7,3,9]

smallest_num=numbers[0]

for i in range(len(numbers)):
    if numbers[i]<smallest_num:
        smallest_num=numbers[i]
print(f"The smallest number is {smallest_num}")
        