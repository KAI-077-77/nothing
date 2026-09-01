#  FIND THE SECOND SMALLEST NUMBER IN A LIST 

num=[]
n=int(input(" Enetr length of the list :"))

for i in range(n):
    x=int(input(" Enter elements of the list :"))
    num.append(x)
print(x)

num.sort()
print(" Second smallest number in the list is :",num[2])