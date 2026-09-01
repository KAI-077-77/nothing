# CRAETE A LIST ONLY CONTAINING EVEN NUMBERS 

num=[]
n=int(input(" Enter the length of the list :"))

for i in range (n):
    x=int(input(" Enter elements :"))
    num.append(x)
print(num)

a=[]

for t in range (n):

    if num[t]%2==0:
        a.append(num[t])

print(a)