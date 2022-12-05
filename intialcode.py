Investments = {
    "VOO": 10,
    "QQQ": 13,
    "VTI": 9.79,
    "SPY": 10
    }

def compound_int(P, r, n, t):
    """
    Function that calculates compound interest.
    """
    value = P * (pow((1 + (r/n)), n * t))
    interest = value - P
    print("Compounded interest is", interest)
    print("Initial investment was", P)
    print("Final value will be", value)

def compound_int_prompts():
    principle = int(input('Enter initial amount: '))
    rate = (float(input("Enter expected interest rate (%) ")))/100
    n_input = (input('Enter compounding period (daily, monthly, or annual): '))
    if n_input == 'annual':
        frequency = 1 
    elif n_input == 'monthly':
        frequency = 12
    elif n_input == 'daily':
        frequency = 365
    time = float(input('Enter years of investment: '))

    compound_int(principle, rate, frequency, time)

compound_int_prompts()