def withdraw_amount(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance
   

balance = withdraw_amount(100, 90)

if (balance <= 50):
    print("deposit money into your account")
else:
    print("your account is in good standing")
