# Using arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings
# Prompt the user for their monthly income
monthly_income = float(input('“Enter your monthly income: '))
# Ask for their total monthly expenses
total_monthly_expenses = float(input('Enter your total monthly expenses: '))
# Calculate the monthly savings by subtracting monthly expenses from the monthly income
monthly_savings = monthly_income - total_monthly_expenses
# Print the monthly savings
print(f'Your monthly savings is $[monthly_savings:.2f]') #format to 2 decimal places
# We are going to project Annual savings
annual_interest_rate = 0.05 #5%
# We calculate the projected savings after one year, incorporating the interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)
# print the projceted savings after including interest
print(f'Projected savings after one year, with interest, is: $[projected_savings].2f') #format to 2 decimal places