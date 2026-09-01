# FIND THE SUM OF ALL EVEN NUNMBERS IN A LIST 

num=[ ]
n=int(input(" Enter the length of the list :"))

for i in range (n):
    x=int(input(" Enter the elements of the list :"))
    num.append(x)

print(num)

sum=0

for t in range (n):

    if num[t]%2==0:
        sum=sum+num[t]

print(sum)