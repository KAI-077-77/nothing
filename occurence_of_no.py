# COUNT HOW MANY TIMES A NUMBER OCCURS IN A LIST

num=[]
n=int(input(" Enter the length of the list :"))

for i in range (n):
    x=int(input(" Enter elements :"))
    num.append(x)

print(num)

c=0
y=int(input(" Enter a number to check :"))

for t in range (n):

    if y==num[t]:
        c=c+1

print(c)