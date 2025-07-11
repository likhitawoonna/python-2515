car_variant="220i M Sport (Petrol) 50.71 Lakh*"
on_road_price=5071412
down_payment=507000
loan_period=5
rate_intr=9.8
loan_amount = on_road_price - down_payment
months = loan_period * 12
monthly_interest_rate = rate_intr / (12*100)
emi = (loan_amount * monthly_interest_rate * ((1+monthly_interest_rate) ** months)) / (((1+monthly_interest_rate) ** months) - 1)
payable_amount = emi * months
print("======================")
print(f"Car Variant: {car_variant}")
print(f"Car Price: {on_road_price}")
print(f"Time Period: {loan_period} years")
print(f"Rate of Interest: {rate_intr}%")
print(f"Initial Down Payment: {down_payment}")

print(f"Total Amount Payable: {payable_amount}")
print(f"Monthly Installment: {emi}")
print(payable_amount)
