monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your monthly expensed: "))
monthly_saving = float(monthly_income -monthly_expense)

projected_savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print(f'Your monthly savings are ${monthly_saving}')
print(f'Projected savings after one year, with interest, is: ${projected_savings}')