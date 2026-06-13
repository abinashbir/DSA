arr=[1,2,3,3,3,4,5,6]
occurance=0
target=int(input("Enter the target in the array [1,2,3,3,3,4,5,6] : "))
for i in range(len(arr)):
    if arr[i]==target:
        occurance=occurance+1
print(occurance)

