loan_amount=int(input("enter the amount:"))

interest_rate=int(input("enter the interest rate:"))

loan_tenure=int(input("enter the monthly tenure:"))

monthly_interest_rate=(interest_rate/12)/100

emi=(loan_amount*monthly_interest_rate*(1+monthly_interest_rate)*loan_tenure)/((1+monthly_interest_rate)*loan_tenure-1)

total_payment=emi*loan_tenure

total_interest=total_payment -loan_amount
print("emi=",emi)

print("total_payment=",total_payment)

print("total_interest=",total_interest)