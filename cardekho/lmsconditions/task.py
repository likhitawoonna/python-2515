
customer_id= int(input("enter id of the customer:    "))
customer_name=input("enter name of the customer: ")
is_customer_premium=input("is premium ? (true/false): ")
is_premium=is_customer_premium=="true"
years_partnership=int(input("enter years of partnership:  "))
deal_stage=input("proposal/negotiation/closed:  ")
deal_value=int(input("enter the deal value: "))
discount=0.0


if is_premium=="true":
    print(f"enter customer id {customer_id}")
    print(f"enter name {customer_name}")
    base_discount=0.10
    print("premium customer with 10percent discount: ")

elif  years_partnership>=3:
    base_discount = 0.05
    print("non premium with 5 percentage discount: ")
else:
    base_discount=0.0
    
match deal_stage:
    case "proposal":
        extra_discount = 0.02
    case "negotiation":
        extra_discount = 0.03
    case "closed":
        extra_discount =0.05
    case _:
        extra_discount = 0.0
final_amount=base_discount+extra_discount
discounted_deal=deal_value*(1-final_amount)
print(f"processing discount for {customer_name}")
print(f"customer id {customer_id}")
print(f"customer name {customer_name}")
print(f"enter years of partner {years_partnership}")
print(f"base fee {deal_value}")
print(f"discount saved {final_amount*100}%")
print(f"final amount {discounted_deal}")
print(f"amount saved:{deal_value-discounted_deal}")





