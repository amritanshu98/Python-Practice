# Read deposit (D) and withdrawal (W) transactions from console. Compute the final balance. E.g. D 300, D 300, W 200, D 100 → 500.

D = [300, 300, 100]
W = [200]

# total_deposit = sum(D)
# total_withdrawl = sum(W)

# final_balance = total_deposit-total_withdrawl

total_deposit = 0
total_withdrawl = 0
final_balance = 0

for d in D:
    total_deposit +=d

for w in W:
    total_withdrawl +=w

final_balance = total_deposit-total_withdrawl 



print(f"FInal Balance: {final_balance}")