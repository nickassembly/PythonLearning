calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"

def validate_and_execute():

        try:
            user_input_number = int(num_of_days_element)
            if user_input_number > 0:
              calculated_value = days_to_units(user_input_number)
              print(calculated_value)
            elif user_input_number == 0:
              print("You entered 0, please enter a valid positive number")
            else:
              print("you entered a 0, this is invalid")

        except ValueError:
          print("Invalid input")

user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days as a comma separated list and I will convert to hours.\n")
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()






