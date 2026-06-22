word='swiss'
arr=[c for c in word]


for c in arr:
    count=0

    for j in arr:
        if c==j:
            count+=1
    if count == 1:
        print(c)
        break
    



# print(arr)