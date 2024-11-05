# List to store calculation history for tracking 
history = []

# Function to display the history of calculations
def show_history():
    if history:
        print("\nCalculation History:")
        for index, calc in enumerate(history, 1):
            print(f"{index}. {calc}")
    else:
        print("\nNo calculations performed yet!")

# Function to add a calculation result to history
def add_to_history(result):
    history.append(result)

# Function to clear the history
def clear_history():
    history.clear()
