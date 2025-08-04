car_variant = "z2E petrol"
on_road_price = 2007695
loan_period_years = 5
rate_of_interest = 8
down_payment = 500000
# simple_interest = (car_price - initial_down_payment) * rate_of_interest * time_period / 100
# total_amount = car_price - initial_down_payment + simple_interest
# monthly_installment = total_amount / (time_period * 12)

# Correct Implementation
loan_amount = on_road_price - down_payment
months = loan_period_years * 12
monthly_interest_rate = rate_of_interest / (12*100)

emi = (loan_amount * monthly_interest_rate * ((1+monthly_interest_rate) ** months)) / (((1+monthly_interest_rate) ** months) - 1)

payable_amount = emi * months

print("======================")
print(f"Car Variant: {car_variant}")
print(f"Car Price: {on_road_price}")
print(f"Time Period: {loan_period_years} years")
print(f"Rate of Interest: {rate_of_interest}%")
print(f"Initial Down Payment: {down_payment}")

print(f"Total Amount Payable: {payable_amount}")
print(f"Monthly Installment: {emi}")