# range(10)

a  = range(10)
print(f"Type pf a: {type(a)}")

for i in range(20):
    if i == 5:
        break
    print(i, end=" ")
print()

for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
print()
print("-" *  10)

for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
else:
    print("Loop ended normally")



# List of fruits
fruits= ["Banana", "Oragne", "Mango", "Grapes", "Pineapple" ]

fruit_go_check = "Banana"

for fruit in fruits:
    if fruit == fruit_go_check:
        print(f"{fruit_go_check} is in list")
        break
else:
    print(f"{fruit_go_check} not in list")


# Happy Hour
print("Why do python devs never get lost")
print("Because they always know where 'in' is")

if fruit_go_check in fruits:
    print(f"{fruit_go_check} is in list")
else:
    print(f"{fruit_go_check} not in list")


# Challenge
print("One line exe")
print(f"{fruit_go_check} is {'in' if fruit_go_check in fruits else 'not in'} the list")
    
