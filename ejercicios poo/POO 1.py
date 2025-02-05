
number= input().strip()
digits_add=0
for digit in number:
  if digit.isdigit():
    digits_add+= int(digit)

print (digits_add)