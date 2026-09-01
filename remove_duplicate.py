# REMOVE ALL DUPLICATE ELEMENTS 

num=[12, 12, 31, 1, 45, 1, 5, 67, 69, 5]

seen=[]

for d in num:
    if d not in seen:
        seen.append(d)
print(seen)