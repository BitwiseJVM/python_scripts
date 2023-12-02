numberList = [15, 85, 35, 89, 125]
#finding a maximum value in the list
maxNum = numberList[0]
for num in numberList:
    if maxNum < num:
        maxNum = num
print(maxNum)

#finding a minimum value in the list
minNum = numberList[0]
for num in numberList:
    if maxNum > num:
        maxNum = num
print(minNum)
