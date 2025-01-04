#for and while

def prikol():
    while True:
        try:
            n = int(input("Enter the n: "))
            if n < 0:
                print("Enter positive number")
                continue
            break
        except ValueError:
            print("Enter int value.")

    if n > 100:
        print("That's a big number!")

    for i in range(0, n+1, 2):
        print(i)

def main():
    while True:
        prikol()

        while True:
            answer = input("Do you want to run program again? (y/n)").strip().lower()
            if answer == 'n':
                return
            elif answer == 'y':
                break
            else:
                print("Enter 'y' or 'n'.")

main()