#Asking user for the principal amount to be invested
n_principalInvestment=float(input('Enter the starting principal: '))

#Asking user for the interest rate in percentage
n_interestRate=float(input('Enter the annual interest rate: '))

#Asking user for # of times compounding occurs per period
n_compounding=float(input('How many times per year is the interest compounded? '))

#Asking user for the number of years/periods
n_numberOfPeriods=float(input('For how many years will the account earn interest? '))

#Converting interest rate% into decimal form
n_interestRate=n_interestRate/100

#Determining our future value by applying the formula; FV=PV(1+r/m)^mt
n_futureValue=n_principalInvestment*(1+(n_interestRate/n_compounding))**(n_compounding*n_numberOfPeriods)

#Displays future value to the user
print(f'At the end of two years you will have: ${n_futureValue:,.2f}')
