age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Valid age and eligible for voting")
else:
    print("Valid age but not eligible for voting")