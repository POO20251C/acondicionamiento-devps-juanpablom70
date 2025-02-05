from posixpath import join
numbers= input() 
numbers_separated=" ".join(numbers.split())
the_inverse=numbers_separated[::-1]
print(the_inverse)