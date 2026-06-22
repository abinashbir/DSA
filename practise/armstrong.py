def is_armstrong(number:int):
    original=number
    last_num=0
    arm_num=0
    while number>0 :
        last_num=number%10
        number=number//10
        arm_num=arm_num + (last_num**3)
    if original==arm_num:
        return "This is a armstrong number"
    else:
        return "This is not a armstrong number"
    
print(is_armstrong(371))

# number = 153
# original=number
# last_num=0
# arm_num=0
# while number>0 :
#     last_num=number%10
#     number=number // 10
#     arm_num = arm_num + (last_num**3)
# if original==arm_num:
#     print("This is a armstrong number")
# else:
#     print("This is not a armstrong number")
