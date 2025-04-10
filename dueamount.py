bill_amount = float(input("enter the total bill amount: "))
amount_paid = float(input("enter the amount paid"))
if amount_paid < bill_amount:
    due_amount = bill_amount - amount_paid
    print(f"customer still owes")
elif amount_paid > bill_amount:
    change = amount_paid - bill_amount
    print(f"customer has overpaid. return {change:.2f}")
else:
    print("bill fully paid no due amount")