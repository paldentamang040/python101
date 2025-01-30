#AML-1213
#In-class-activity1
#Palden Tamang
#Januart 23 2025

#Question 1:
print("\nQUESTION 1")
food_price=int(input("\nEnter the price of food: "))

TIP=18
HST=13

tip_amount= (TIP*food_price)/100
hst_amount= (HST*food_price)/100

total_amount0= food_price + tip_amount + hst_amount
final_amount0= format(total_amount0,".2f")

print("\nThe amount to be tipped is ",tip_amount)
print("\nThe HST to paid is ",hst_amount)
print("\nThe total amount to be paid for the food is ", final_amount0)

print("\nQUESTION 1 completed\n")

print("#############################################################################################################")

# Question 2:
print("\nQUESTION 2")
principal_amount=float(input("\nEnter the amount of money originally deposited into the account: "))
annual_interest_rate= float(input("\nEnter the annual interest rate paid by the account: "))

times_interest_compounded_per_year= int(input("\nEnter the number of times per year that the interest is compounded(12 for monthly compound or 4 for quarterly): "))
account_left_in_yrs= int(input("\nEnter the number of years that the account will be left to earn interest: "))

total_amount= principal_amount*((1+((annual_interest_rate/100)/times_interest_compounded_per_year))
                                **(times_interest_compounded_per_year*account_left_in_yrs))

final_amount=format(total_amount,".2f")

print("\nThe amount of money in the account after",account_left_in_yrs,"years is: $",final_amount)


print("\nQUESTION 2 completed")
