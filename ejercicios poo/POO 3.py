text = input() 
text = text.replace(" ", "").lower()  


if text == text[::-1]:  
    print("yes")  
else:  
    print("No")  