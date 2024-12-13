#Define main function
def main():

    #Initialize main empty list
    floatList = []


    #Call input function for initial use. Also add input value to list with append
    fListInput = getFloatInput("Enter property sales value: ")
    floatList.append(fListInput)


    #Creates loop asking user if they would like to put another input in. If so, repeat the lines above
    while True:
        YorN = input(f'Enter another value Y or N: ')
        if YorN.upper() == 'N':
             break
        elif YorN.upper() == 'Y':
            fListInput = getFloatInput("Enter property sales value: ")
            floatList.append(fListInput)
            
                
    #Sort list from least to greatest, and initalize a total input value for our list.
    floatList.sort()
    totalInputs = int(len(floatList))

    
    #Empty line for organizational/neatness purposes
    print(f'\n')


    #Create for loop that restarts one time for how many inputs are in the list
    for propertyNumber in range(totalInputs):
        print(f'Property {propertyNumber + 1}: ${floatList[propertyNumber]:,.2f}')


    #Display min, max, total, and average in print formats with sum function and indexing
    print(f'\nMinimum:    ${floatList[0]:,.2f}')
    print(f'Maximum:    ${floatList[-1]:,.2f}')
    print(f'Total:      ${sum(floatList):,.2f}')
    print(f'Average:    ${sum(floatList) / totalInputs:,.2f}')


    #Use median function and use the list and total inputs as parameters. 
    getMedian(floatList,totalInputs)


    #Display commission with sum function and multiplication
    print(f'Commission: ${sum(floatList) * .03:,.2f}')
    

#Create float input loop function that accounts for data validation, and uses prompt as a parameter
def getFloatInput(prompt):
    while True:
        try:
            result = float(input(prompt))
            if result > 0:
                return result
            elif result <= 0:
                print(f'Input a number that is greater than zero.')
        except ValueError:
            print(f'Input a number that is greater than zero.')


#Create median function where even inputs (if) has different math than odd inputs (else)
def getMedian(userList,total):
    if (int(total % 2)) == 0:
        index = int(total / 2)
        firstValue = userList[index]
        indexTwo = index - 1
        secondValue = userList[indexTwo]
        result = float((firstValue + secondValue) / 2)
        print(f'Median:     ${result:,.2f}')
        return result
    else:
        index = int(total / 2)
        result = userList[index]
        print(f'Median:     ${result:,.2f}')
        return result
    

#Call main function.                        
main()