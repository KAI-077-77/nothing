# FIND THE SECOND LARGEST NUMBER IN A LIST 
num=[]
n=int(input(" Enter thr length of the list :"))

for i in range (n):
    x=int(input(" Enter elements of thr list :"))
    num.append(x)
print(num)

num.sort()
print(" Second largest number is :",num[-2])