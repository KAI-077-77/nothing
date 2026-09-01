# SEPARATE EVEN AND ODD NUMBERS 

num = [0, 7, 12, 3, 18, 5, 24, 9, 16, 11, 20]

even=[]
odd=[]

for d in num:

    if d % 2==0:
        even.append(d)
    else :
        odd.append(d)

print(even)
print(odd)