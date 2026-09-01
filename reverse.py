# REVERESE A LIST WITHOUT USING REEVERRSE AND SLICING 

num = [1, 2, 3, 4, 5]

new = []

for i in range(len(num)-1, -1, -1):
    new.append(num[i])

print(new)