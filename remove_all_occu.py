# REMOVE ALL OCCURENCE OF AN NUMBER FROM LIST 

num=[]
n=int(input(" Enter the length of the list :"))

for i in range (n):
    x=int(input(" Enter elements :"))
    num.append(x)

print(num)

a=int(input(" Enter a number to remove that :"))
new=[]

for t in range (n):

    if num[t]!=a:
        new.append(num[t])

print(" After removing the new list is :",new)