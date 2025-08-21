#Barry

def sorting_game():
    print("\n--- Number Sorting Game ---")
    numbers = []
    while len(numbers) < 5:
        try:
            num = int(input(f"Enter number {len(numbers) + 1}: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    order = input("Sort in ascending or descending order? (asc/desc): ").lower()
    if order == "asc":
        numbers.sort()
        print("Sorted in ascending order:", numbers)
    elif order == "desc":
        numbers.sort(reverse=True)
        print("Sorted in descending order:", numbers)
    else:
        print("Invalid option. Displaying original list:", numbers)

sorting_game()
