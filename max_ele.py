# FIND THE MAXIMUM ELEMNET IN A LIST WITHOUT USING MAX FUNCTION 

num=[]
n=int(input(" Enter length of the list :"))

for i in range (n):
    x=int(input(" Enter the elements of the list :"))
    num.append(x)

print(num)

max=num[0]

for t in range(n):

    if num[t] > max :
        max=num[t]

print(num[t])