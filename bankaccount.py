
account_holder = "Alex"
account_number = 1001
balance = 500


print("Account Holder:", account_holder)
print("Account Number:", account_number)
print("Balance: #" + str(balance))

deposit_amount = 200
balance = balance + deposit_amount
print("After deposit, balance is: #" + str(balance))


withdrawal_amount = 150
balance = balance - withdrawal_amount
print("After withdrawal, balance is: #" + str(balance))