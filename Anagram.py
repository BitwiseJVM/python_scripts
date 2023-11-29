#Anagram means all the letters of two strings are matching.
str1=input("enter the first string:")
str2=input("enter the second string:")

s1=list(str1.upper())
s2=list(str2.upper())
s1.sort(),s2.sort()

if(s1==s2):
    print("True")
else:
    print("false")