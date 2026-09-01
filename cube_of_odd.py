# Create a new list containing cubes of odd numbers only

num=[2, 4, 6, 5, 12]

c=[]

for d in num:
    if d % 2 != 0 :
        c.append(d**3)

print(c)