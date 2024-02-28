#reverse an integer

temp=int(input("enter the integer:"))
#12345
reverse=0

while (temp!=0):
    reverse=reverse*10+temp%10
    temp=temp//10

print(reverse)

