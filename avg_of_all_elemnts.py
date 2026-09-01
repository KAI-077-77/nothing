# FIND THE AVERAGE OF LIST ELEMENTS 

num=[]
n=int(input(" Eneter the length of the list :"))

for i in range (n):
    x=int(input(" Enter elemnts of the list :"))
    num.append(x)
print(num)

s=0
for t in range (n):
    s=s+num[t]
avg=s/n
print("Average :",avg)