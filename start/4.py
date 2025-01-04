#lists

numbers = input("Enter the numbers separated by commas: ")

try:
    numbers_list = [int(num.strip()) for num in numbers.split(",")]
    print("Your list: ", numbers_list)

    numbers_list.append(10)
    print("Your list after adding 10 to the end: ", numbers_list)

    if numbers_list:  # checking if the list is not empty
        numbers_list.pop(0)
    print("Your list after removing the 1st number: ", numbers_list)

    num_list_2 = []
    for i in numbers_list:
        i = i*2
        num_list_2.append(i)
    print("Your list after doubling elements: ", num_list_2)

        # OR

    num_list_2 = [i * 2 for i in numbers_list]
    print("Your list after doubling elements:", num_list_2)

except ValueError:
    print("Enter only numbers separated by commas.")


