#Create loop asking user for deposit amount
#add ValueError exception and display error message for any number zero or less, and non numeric values.
while True:
    try:
        n_Deposit = float(input(f'What is the original deposit?: '))
        if n_Deposit > 0:
            break
    except ValueError:
        pass
    print(f'Input must be a positive numeric value.')


#Create loop asking user for interest rate percentage
#add ValueError exception and display error message for any number zero or less, and non numeric values.

while True:
    try:
        n_InterestRatePercentage = float(input(f'What is the interest rate?: '))
        if n_InterestRatePercentage > 0:
            break
    except ValueError:
        pass
    print(f'Input must be a positive numeric value.')


#Make necessary conversions to change interest rate into monthly interest rate
n_InterestRatePercentage /= 100
n_MonthlyInterestRate = n_InterestRatePercentage/12



#Create loop asking user for number of months
#add ValueError exception and display error message for any number zero or less, and non numeric values.
while True:
    try:
        n_NumOfMonths = float(input(f'What is the number of months?: '))
        if n_NumOfMonths > 0:
            break
    except ValueError:
        pass
    print(f'Input must be a positive numeric value.')


#Create loop asking user for goal amount
#add ValueError exception and display error message for any number less than zero, and non numeric values.
while True:
    try:
        n_Goal = float(input(f'What is the goal?: '))
        if n_Goal >= 0:
            break
    except ValueError:
        pass
    print(f'Input must be a positive numeric value.')





#Calulate compound interest for each month, then display until n_NumOfMonths is reached
n_Month = 1
n_AccountBalance = n_Deposit
while n_Month <= n_NumOfMonths:
    n_InterestForMonth = (n_AccountBalance * n_MonthlyInterestRate)
    n_AccountBalance += n_InterestForMonth
    print(f'Month: {n_Month} Account Balance is: ${n_AccountBalance:,.2f}')
    n_Month += 1




#if the goal amount is greater than zero, calculate how many months it will take to reach goal, then print
#if goal amount is zero, do nothing
n_TotalMonths = 0
n_AccountBalance = n_Deposit
if n_Goal > 0:
    while n_AccountBalance < n_Goal:
        n_InterestForMonth = (n_AccountBalance * n_MonthlyInterestRate)
        n_AccountBalance += n_InterestForMonth
        n_TotalMonths += 1
    print(f'It will take: {n_TotalMonths} months to reach the goal of {n_Goal:,.2f}')

    
 









    
                            
     
        





                    
