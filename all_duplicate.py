# FIND ALL DUPLICATE ELEMEMNTS IN A LIST 

num=[12, 34, 1, 12, 2, 5, 6, 5, 34]

seen=[]
dup=[]

for d in num:
    if d not in seen:
        seen.append(d)
    else:
        dup.append(d)

print(" Duplicate elements are :",dup)