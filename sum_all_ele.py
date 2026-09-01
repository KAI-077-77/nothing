# CALCULATE THE SUM OF ALL NUMBERES IN A LIST 

num=[]
n=int(input(" Enter length of the list :"))

for i in range (n):
    x=int(input(" Enter the elements of the list :"))
    num.append(x)

print(num)

sum=0

for t in range (n):
    sum=sum+num[t]

print(sum)