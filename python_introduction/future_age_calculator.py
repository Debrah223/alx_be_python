# Performing a simple arithmetic operation to calculate the user’s age in a future year.
# We will prompt the user to enter their current age
current_age = int(input('How old are you? '))
# We shall calculate the age in 2050 (Assuming the current year is 2023)
future_age = current_age + (2050-2023)
# Print the user's age in the correct format
print(f'In 2050, you will be [future_age] years old')