calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    condition_check = num_of_days > 0
    print(type(condition_check))

    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"
    elif num_of_days == 0:
        return "You entered 0, please enter a valid positive number"
    else:
        return "You entered a negative value, no conversion available"

user_input = input("Enter a number of days to convert to hours.\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)

