monthly_contribution = 500
current_balance = 5000
investment_goal = 250000

months_elapsed = 0 
annual_return_rate = 0.08  # 8% annual return

while current_balance < investment_goal:
    current_balance += monthly_contribution
    if months_elapsed % 12 == 11:  # Apply returns annually
        returns = current_balance * annual_return_rate
        current_balance += returns
    months_elapsed += 1

print(f"It will take {months_elapsed} months to reach your goal.")