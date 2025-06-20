import math
name = "Alice"
age = 20

print("CF7")
print("PI:", math.pi)

print(name, "is", age, "years old")

# print(name + "is " + age + " years old")
print(name + " is " + str(age) + " years old")

# python 2 style
print()
print("Python2 style")
print("PI = %6.2f"  %math.pi )
print("%s is %d years old" %(name, age))

print("\nPython3 style")
print("Age is {0:2d}".format(age))
print("PI is {0:.3f}".format(math.pi))

print("PI = {0:.3f} and age = {1}".format(math.pi, age))


#Alice is 20 years old**
print("{0}  is  {1}  years old".format(name, age), end="**")

# f string
print(f"{name} is {age} years old.")