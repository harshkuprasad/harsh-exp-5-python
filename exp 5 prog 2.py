d = dict(eval(input("Enter a dictionary value: ")))
s = []
s1 = []

for v in d.keys():
    s.append(v)

for v in d.values():
    s1.append(v)

mv = s1[0]
mk = s[0]

for i in range(1, len(s)):
    if s1[i] > mv:
        mv = s1[i]
        mk = s[i]

print("The key with maximum value is:", mk)
