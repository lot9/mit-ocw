# ------------------------------------------------------------------------------------------------------------
#
# Write a program that calculates the minimum fixed monthly payment need in order to pay off a credit card
# balance within 12 months. (will not be dealing with a minimum monthly payment rate)
#
# ------------------------------------------------------------------------------------------------------------

# --- Constants ---
MONTHS_PER_YEAR = 12


# --- Functions ---
def GetFinalBalance(init_balance, annual_rate, monthly_payment):
    """Calculates the outstanding balance left over at the end of the year.
        - returns tuple of the form (final_balance, month) """
    balance = init_balance
    monthly_rate = annual_rate / MONTHS_PER_YEAR
    for i in range(MONTHS_PER_YEAR):
        balance = balance * (1 + monthly_rate) - monthly_payment
        if balance <= 0.0:
            break
    return (balance, i+1)


# --- Main ---
# - get input from user -
outstanding_balance = float( raw_input("Enter the outstanding balance on your credit card: ") )
annual_interest_rate = float( raw_input("Enter the annual credit card interest rate as a decimal: ") )

# - initialize loop variables -
step_size = 10.0
payment = step_size
result = GetFinalBalance(outstanding_balance, annual_interest_rate, payment)
while result[0] > 0.0:
    payment = payment + step_size
    result = GetFinalBalance(outstanding_balance, annual_interest_rate, payment)

# - print results -
print "RESULT"
print "Monthly payment to pay of debt in 1 year:", int(payment)
print "Number of months needed:", result[1]
print "Balance:", round(result[0], 2)
