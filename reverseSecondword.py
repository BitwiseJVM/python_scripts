#Question: reverse every word that is present at even position(index)
#input : Jayesh is Kind person
#output : sheyaJ is dnik person

def revsecondword(user_input):
    lst=user_input.split()
    i=0
    final=[]
    while i <len(lst):
        if i%2==0:
            final.append(lst[i][::-1])

        else:
            final.append(lst[i])
            
        i+=1

    return " ".join(final)

userinput=input()
output=revsecondword(userinput)
print(output)
