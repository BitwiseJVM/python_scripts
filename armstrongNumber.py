#check Armstrong number
#123
num=int(input("enter the number"))
total=0
number=num
while num!=0:
    total+=(num%10)*(num%10)*(num%10)
    num=num//10

print(total)
if total==number:
    print("yes")
else:
    print("no")