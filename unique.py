# PRINT UNIQUE ELEMENTS ONLY 

num = [13, 1, 3, 6, 5, 6, 13, 34, 2, 2]

uni=[]

for d in num:
    if num.count(d)==1:
        uni.append(d)

print(uni)