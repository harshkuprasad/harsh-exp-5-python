d = dict(eval(input("Enter a dictionary value: ")))
temp = []
res = dict()
for key, val in d.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
print(res)        
