s=set(eval(input("Enter a set element:")))
s1=set()
for i in range(1, len(s)+1):
    s1.update(s)
print("Updated set is:", s1)
