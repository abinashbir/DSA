# def add_score(name,score):
#     l1.append(name)
#     l1.append(score)

# def add_list(l1):
#     l2.append(l1)
#     print(l2)

# l1=[]
# l2=[]

python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] 

high =0
second_high=0
for i in range(len(python_students)):
    # print(python_students[i][1])

    if python_students[i][1]>high:
        high=python_students[i][1]
    
for i in range(len(python_students)):
    if python_students[i][1]>second_high and python_students[i][1]<high:
        second_high=python_students[i][1]

for i in range(len(python_students)):
    if python_students[i][1]==second_high:
        print(python_students[i][0])
# print(high)
# print(second_high)


