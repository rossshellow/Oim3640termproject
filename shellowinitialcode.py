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
    ROI = 100 * (value - P) / (P)

    print(f"The compounded interest is {round(interest, 2)}")
    print("Initial investment was", P)
    print(f"The final value will be {round(value, 2)}")
    print(f"Your Return on Investment (ROI) would be: {round(ROI, 2)} % ")

def compound_int_prompts():

    principle = int(input('Enter how much you would like to invest: '))
    #rate = (float(input("Enter expected interest rate (%) ")))/100
    # What if the input chose the name of the stock one wants to invest in and based on the choice, the rate for that stick is used when
    # the code runs
    r_input = (input('From the following options, enter which stock you would like to invest in: VOO, QQQ, VTI,or SPY: ')) 
    r_input = r_input.lower()
    if r_input == 'voo':
        rate = 10/100
    elif r_input == 'qqq':
        rate = 13/100
    elif r_input == 'vti':
        rate = 9.79/100
    elif r_input == 'spy':
        rate = 10/100
    
    n_input = (input('Enter your desired compounding period: Daily, monthly, or annually: '))
    n_input = n_input.lower()
    if n_input == 'annually':
        frequency = 1 
    elif n_input == 'monthly':
        frequency = 12
    elif n_input == 'daily':
        frequency = 365
    time = float(input('Enter years of investment: '))

    compound_int(principle, rate, frequency, time)

compound_int_prompts()
