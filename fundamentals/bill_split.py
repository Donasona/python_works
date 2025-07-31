bill_amount = int(input("enter bill amount:"))

dines_count = int(input("enter dines_count:"))

tip_percentage=12
GST_percentage = 8

tip = (tip_percentage/100)*bill_amount

gst = (GST_percentage/100)*bill_amount

total_amount=bill_amount+tip+gst

individual_split = total_amount/dines_count

print( "tatal_amount =",total_amount)

print("individual_split =",individual_split)
