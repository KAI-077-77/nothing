# COUNT HOW MANY EVEN NUMBERS ARE THERE IN A LIST

num=[]
n=int(input(" Enter the length of the list :"))

for i in range (n):
    x=int(input(" Enter the elements of the list :"))
    num.append(x)

print(num)

for t in range (n):

    if num[t]%2==0:
        print(num[t])