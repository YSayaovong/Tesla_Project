def checkDriverAge(age=0):
    # Convert the age to an integer, in case it's passed as a string
    age = int(age)
    
    if age < 18:
        print("Sorry, you are too young to drive this car. Powering off.")
    elif age > 18:
        print("Powering On. Enjoy the ride!")
    else:  # This handles the case when age is exactly 18
        print("Congratulations on your first year of driving. Enjoy the ride!")

# Call the function with a given age
checkDriverAge(92)  # Example call

# Call the function without any arguments, will use the default age
checkDriverAge()  # Default age is 0
