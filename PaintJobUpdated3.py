#Imports the math module for rounding purposes later
import math


#Creating the main function and calling all other functions from here
def main():

    #Function that gives float input values to the variables
    n_SquareFeet = getFloatInput("Enter wall space in square feet: ")
    n_PaintPrice = getFloatInput("Enter paint price per gallon: ")
    n_FeetPerGallon = getFloatInput("Enter feet per gallon: ")
    n_LaborPerGallon = getFloatInput("How many labor hours per gallon: ")
    n_LaborCharge = getFloatInput("Labor charge per hour: ")

    #Input job state and last name
    s_State = input("State job is in: ")
    s_LastName = input("Customer Last Name: ")

    #Opens text file and creates variable to put into the below functions
    paint_job_txt = open(f'{s_LastName}PaintJobOutput.txt','w')

    #Main calculation and output functions. All math done here. 
    n_TotalGallons = getGallonsOfPaint(n_SquareFeet, n_FeetPerGallon, paint_job_txt)
    
    n_TotalLaborHours = getLaborHours(n_LaborPerGallon, n_TotalGallons, paint_job_txt)

    n_TotalPaintCost = getPaintCost(n_PaintPrice, n_TotalGallons, paint_job_txt)

    n_TotalLaborCost = getLaborCost(n_TotalLaborHours, n_LaborCharge, paint_job_txt)

    n_TotalSalesTax = getSalesTax(s_State, n_TotalLaborCost, n_TotalPaintCost, paint_job_txt)

    showCostEstimate(n_TotalPaintCost, n_TotalLaborCost, n_TotalSalesTax, paint_job_txt)

    #Close the text file after writing to it in the above functions
    #Display message to user that notifies them their file was created.
    paint_job_txt.close()
    print(f'File: {s_LastName}PaintJobOutput.txt was created.')


    

#Gives input values to all the first float variables that we need
#Also uses value error loop to make sure input is valid.
def getFloatInput(userInput):
    while True:
        try:
            result = float(input(userInput))
            if result > 0:
                return result
        except ValueError:
            pass
        print(f'Input must be a positive numeric value.')

#Calculates the total amount of gallons needed, also rounds up to nearest integer.
def getGallonsOfPaint(sqFeet, feetPerGallon, txtFile):
    result = sqFeet/feetPerGallon
    print(f'Gallons of paint: {int(math.ceil(result))}')
    txtFile.write(f'Gallons of paint: {int(math.ceil(result))}\n')
    return math.ceil(result)


#Calculates the total amount of labor hours needed
#Uses return from the getGallonsOfPaint function
def getLaborHours(laborPerGallon, totalGallons, txtFile):
    result = float(laborPerGallon*totalGallons)
    print(f'Hours of labor: {result:,.1f}')
    txtFile.write(f'Hours of labor: {result:,.1f}\n')
    return result

#Calculates the total cost of the labor
#Uses return from the getLaborHours function
def getLaborCost(totLaborHours, laborCharge, txtFile):
    result = float(totLaborHours*laborCharge)
    print(f'Labor charges: ${result:,.2f}')
    txtFile.write(f'Labor charges: ${result:,.2f}\n')
    return result


#Calculates the total cost of the paint
#Uses return from the getGallonsOfPaint function
def getPaintCost(paintPrice, totalGallons, txtFile):
    result = float(paintPrice*totalGallons)
    print(f'Paint charges: ${result:,.2f}')
    txtFile.write(f'Paint charges: ${result:,.2f}\n')
    return result


#Determines what state the user inputted for s_State, and gives it a tax rate value.
#Calculates the total sales tax
def getSalesTax(state, totLaborCost, totPaintCost, txtFile):
    if state.upper() == "MA":
        taxRate = .0625

    elif state.upper() == "CT":
        taxRate = .06

    elif state.upper() == "ME":
        taxRate = .085

    elif state.upper() == "RI":
        taxRate = .07

    elif state.upper() == "VT":
        taxRate = .06

    else:
        taxRate = 0

    result = float(taxRate*(totLaborCost + totPaintCost))
    print(f'Tax: ${result:,.2f}')
    txtFile.write(f'Tax: ${result:,.2f}\n')
    return result


#Calculates the total cost of the paint job.
def showCostEstimate(totPaintCost, totLaborCost, totSalesTax, txtFile):
    result = float(totPaintCost + totLaborCost + totSalesTax)
    print(f'Total cost: ${result:,.2f}')
    txtFile.write(f'Total cost: ${result:,.2f}\n')

    
    
#Calls the main function   
main()


    
    
