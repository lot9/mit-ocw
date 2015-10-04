# ------------------------------------------------------------------------------------------------------------
#
# Write a program that calculates the minimum fixed monthly payment need in order to pay off a credit card
# balance within 12 months. (will not be dealing with a minimum monthly payment rate)
#
# ------------------------------------------------------------------------------------------------------------

# --- Constants ---
EPSILON = 0.01
MONTHS_PER_YEAR = 12


# --- Functions ---
def GetFinalBalance(init_balance, annual_rate, monthly_payment):
    """Calculates the outstanding balance left over at the end of the year.
        - returns tuple of the form (final_balance, month) """
    balance = init_balance
    monthly_rate = annual_rate / MONTHS_PER_YEAR
    for i in range(MONTHS_PER_YEAR):
        balance = round(balance * (1 + monthly_rate) - monthly_payment, 2)
        if balance <= 0.0:
            break
    return (balance, i+1)


# --- Main ---
# - get input from user -
outstanding_balance = float( raw_input("Enter the outstanding balance on your credit card: ") )
annual_interest_rate = float( raw_input("Enter the annual credit card interest rate as a decimal: ") )

# - initialize loop variables -
low = outstanding_balance / 12.0
high = (outstanding_balance * ((1 + (annual_interest_rate / 12.0)) ** 12.0)) / 12.0
while True:
    # - update loop variables -
    payment = (low + high) / 2.0
    result = GetFinalBalance(outstanding_balance, annual_interest_rate, payment)
    
    # - bisect the search space -
    if high - low < (EPSILON / 2.0):
        payment = round(payment + 0.004999, 2)
        result = GetFinalBalance(outstanding_balance, annual_interest_rate, payment)
        break
    elif result[0] < 0.0:
        high = payment
    else:
        low = payment

# - print results -
print "RESULT"
print "Monthly payment to pay of debt in 1 year:", payment
print "Number of months needed:", result[1]
print "Balance:", round(result[0], 2)
