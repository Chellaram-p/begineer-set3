import re
s = input("Enter the string")
k = len(s) - len( re.findall('[\w]', s) )
print("the no of special characters are",k)
