try:
    num = int(input("Enter an integer:"))
    print("You have entered a valid integer of " +str(num) + ".")

except ValueError:
    print("You entered an invalid integer. Please enter a valid integer.")
