# ------------------------------------------------------------------------------------------------------------
# 
# Write a program to calculate the credit card balance after one year if a person only pays the minimum
# monthly payment required by the credit card company each month.
#
# For each month, print the minimum monthly payment, remaining balance, and principle paid in the
# format shown in the test cases below. All numbers should be rounded to the nearest penny. Finally,
# print the result, which should include the total amount paid that year and the remaining balance.
#
# ------------------------------------------------------------------------------------------------------------

# --- Constants ---
MONTHS_PER_YEAR = 12


# --- Functions ---
def GetRemainingBalance(balance, principal_paid):
    return balance - principal_paid

# --- Main ---

# - get user input -
outstanding_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
minimum_monthly_payment_rate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))

# - declare loop variables -
total_paid = 0.0

# - iterate over each calendar month -
for i in range(MONTHS_PER_YEAR):
    
    # calculate results for this month
    minimum_monthly_payment = round(minimum_monthly_payment_rate * outstanding_balance, 2)
    
    interest_paid = round((annual_interest_rate / MONTHS_PER_YEAR) * outstanding_balance, 2)
    principal_paid = round(minimum_monthly_payment - interest_paid, 2)
    
    outstanding_balance = round(outstanding_balance - principal_paid, 2)
    
    # update loop variables
    total_paid = round(total_paid + minimum_monthly_payment, 2)
    
    # print results for this month
    print "Month:", i+1
    print "Minimum monthly payment: $" + str(minimum_monthly_payment)
    print "Principle paid: $"  + str(principal_paid)
    print "Remaining balance: $" + str(outstanding_balance)

# - print the final result -
print "RESULT"
print "Total amount paid: $" + str(total_paid)
print "Remaining balance: $" + str(outstanding_balance)
