#str = "h3110 23 cat 444.4 rabbit 11 2 dog"
str = "1 , 2 , 3 ; 4 , 5 , 6"
str = [int(s) for s in str.split() if s.isdigit()]

print(type(str))
print(str)


