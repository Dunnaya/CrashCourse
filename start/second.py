#conditions (if/elif/else) and logical operators

def age_check():
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Eblo? Enter int.")

    if age < 0:
        print("Autist?")
    elif age < 18:
        print("Soberi penal")
    elif age <= 70:
        print("You're boring now")
    else:
        print("Hahahah plesenb")

while True:
    age_check()

    answer = input("Do you want to check it again? (y/n)").strip().lower()
    if answer == 'n':
        break;
    elif answer != 'y':
        print("Pridurok")
        break
