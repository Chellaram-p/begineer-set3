s = input("Enter the string")
d=0
for c in s:
   if c.isdigit():
        d=d+1
print("numeric characters", d)
