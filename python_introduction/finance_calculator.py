# Using arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings
# Prompt the user for their monthly income
monthly_income = float(input('Enter your monthly income: '))
# Ask for their total monthly expenses
monthly_expenses = float(input('Enter your total monthly expenses: '))
# Calculate the monthly savings by subtracting monthly expenses from the monthly income
monthly_savings = monthly_income - monthly_expenses
# Print the monthly savings
print(f'Your monthly savings are $[monthly_savings:.2f]') #format to 2 decimal places
# We are going to project Annual savings
annual_interest_rate = 0.05 #5%
# We calculate the projected savings after one year, incorporating the interest
annually_savings = monthly_savings * 12
projected_savings = annually_savings + (annually_savings * 0.05)
#print monthly savings
print(f'Your monthly savings are $[monthly_savings:.2f]')
# print the projceted savings after including interest
print(f'Projected savings after one year, with interest, is: $[projected_savings :.2f]') #format to 2 decimal places