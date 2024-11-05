from operations import add, subtract, multiply, divide, exponent, modulus
from history import show_history, add_to_history, clear_history

def calculator():
    # Dictionary mapping operation names to functions
    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide),
        '5': ('Exponent', exponent),
        '6': ('Modulus', modulus)
    }

    print("Welcome to Zinhle's Unique Calculator!")
    print("Available operations:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5/6) or 'H' for history, 'C' to clear history, 'Q' to quit: ").strip().lower()

        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == 'h':
            show_history()
            continue
        elif choice == 'c':
            clear_history()
            print("History cleared.")
            continue
        elif choice in operations:
            operation_name, operation_func = operations[choice]
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            result = operation_func(num1, num2)
            result_text = f"{num1} {operation_name} {num2} = {result}"
            add_to_history(result_text)
            print(result_text)
        else:
            print("Invalid input! Please select a valid operation.")

calculator()