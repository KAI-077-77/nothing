# SEARCH A NUMBER IN A LIST 

num=[]
n=int(input(" Enter length of the list :"))

for i in range (n):
    x=int(input(" Enter elements of the list :"))
    num.append(x)
print(num)

a=int(input(" Enter a number for searching :"))
found=False       # it's means i haven't found the number 

for t in range (n):

    if num[t]==a:
        found=True

if found :
    print(" Nummber is found at ",t)
else:
    print(" Number is not found ")
