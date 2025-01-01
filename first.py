name = input("Enter your name: ")
age = int(input("Enter your age: "))

#input processing example
while True:
    try:
        fav_num = int(input("Enter your favorite number: "))
        break
    except ValueError:
        print("Eblan? Enter int value.")

print("Hello " + name)
print("In 10 years you will be "  + str(age + 10))
print(f"Your fav number doubled is {fav_num*2}")