s=input("enter a string:")
firstchar=s[0]
s=s.replace(firstchar,'$')
s=s.replace('$',firstchar,1)
print(s)
