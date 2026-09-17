x = list(eval(input("Enter the list:")))
y = int(input("Enter the element you want to search:"))
z = lambda x: (x == y)
found = False
for e in x:
    if z(e):
        found = True
        break
if found:
    print(y, "is present in the list.")
else:
    print(y, "is not present in the list.")
    
    
