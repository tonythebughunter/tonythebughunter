import random
upper="ABCDEFGHIJKLMNOQRSTUVWXYZ"
lower="abcefghijklmnopqrstuvwxyz"
numbers="0123456789"
special="!@#$%^&*()-+{}?/"
length=15
add=upper+lower+numbers+special
password="".join(random.sample(add,length))
print("password: " + password)
