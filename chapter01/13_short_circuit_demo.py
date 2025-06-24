name = "Bob"

print("-----or------")

valid_user = None or "User" # None is false so it goes to the next

print("Hello", valid_user)

print("-" * 20)

valid_user = name  or "User"
print("Hello", valid_user)


print("------and-------")

email = "example@mail.com"

valid_email = email and email != ""

print("Valid email:", valid_email)

if email:
    print(f"Hello { valid_user}, your email is: {email}")
else:
    print(f"Hello {valid_user}, please provide your email")
