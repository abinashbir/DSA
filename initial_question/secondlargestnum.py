numbers=[2,5,1,7,3,9]

largest=0

sec=0

for i in range(len(numbers)):
    if numbers[i]>largest:
        sec=largest  
        largest=numbers[i]
    elif sec != largest and numbers[i] > largest :
        sec = largest   

       

       

print(f"The second largest number is {sec} and the largest number is {largest}")
