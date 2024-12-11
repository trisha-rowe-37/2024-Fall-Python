#Asks user for their name, creates variable
s_Name=str(input(f'Name of person that we are calculating the grades for: '))


#Asks user to input their test scores and converts each value to integers
n_TestOne=int(input(f'Test 1: '))

n_TestTwo=int(input(f'Test 2: '))

n_TestThree=int(input(f'Test 3: '))

n_TestFour=int(input(f'Test 4: '))


#Determines if one or multiple of answers were less than zero. If so, terminate program and display message
#If not, ask user if they want to drop the lowest grade and create a user input variable
if n_TestOne<0 or n_TestTwo<0 or n_TestThree<0 or n_TestFour<0:
    print(f'Test scores must be greater than zero.')
    exit()

else:
    s_UserInput=str(input(f'Do you wish to drop the lowest grade? (Y) for yes, (N) for no: '))


#Determines whether the user selected Y, or N. If Y, remove the lowest grade, average the rest, and display to user
#If two or more numbers have lowest grade, only remove one
#If N, average all four test scores and display to user
#If neither, display error message and end program
if s_UserInput.upper()=='Y':
    
    if n_TestOne<n_TestTwo and n_TestOne<n_TestThree and n_TestOne<n_TestFour:
        n_Average=float((n_TestTwo+n_TestThree+n_TestFour)/3)
        print(f"{s_Name}'s test average is: {n_Average:.1f}")
        
    elif n_TestTwo<n_TestOne and n_TestTwo<n_TestThree and n_TestTwo<n_TestFour:
        n_Average=float((n_TestOne+n_TestThree+n_TestFour)/3)
        print(f"{s_Name}'s test average is: {n_Average:.1f}")
        
    elif n_TestThree<n_TestOne and n_TestThree<n_TestTwo and n_TestThree<n_TestFour:
        n_Average=float((n_TestOne+n_TestTwo+n_TestFour)/3)
        print(f"{s_Name}'s test average is: {n_Average:.1f}")

    elif n_TestFour<n_TestOne and n_TestFour<n_TestTwo and n_TestFour<n_TestThree:
        n_Average=float((n_TestOne+n_TestTwo+n_TestThree)/3)
        print(f"{s_Name}'s test average is: {n_Average:.1f}")

    elif n_TestOne==n_TestTwo or n_TestOne==n_TestThree or n_TestOne==n_TestFour:
        n_Average=float((n_TestTwo+n_TestThree+n_TestFour)/3)
        print(f"{s_Name}'s test average is: {n_Average:.1f}")

    elif n_TestTwo==n_TestThree or n_TestTwo==n_TestFour:
        n_Average=float((n_TestOne+n_TestThree+n_TestFour)/3)
        print(f"{s_Name}'s test average is: {n_Average:.1f}")

    elif n_TestThree==n_TestFour:
        n_Average=float((n_TestOne+n_TestTwo+n_TestThree)/3)
        print(f"{s_Name}'s test average is: {n_Average:.1f}")


elif s_UserInput.upper()=='N':
    n_Average=float((n_TestOne+n_TestTwo+n_TestThree+n_TestFour)/4)
    print(f"{s_Name}'s test average is: {n_Average:.1f}")

else:
    print(f'Enter "Y" or "N", to drop the lowest grade.')
    exit()


#Once the average score has been calculated, determine which grade the average qualifies for and then display message
if n_Average>=97:
    print(f'Letter grade for the test is: A+')

elif n_Average>=94 and n_Average<97:
    print(f'Letter grade for the test is: A')

elif n_Average>=90 and n_Average<94:
    print(f'Letter grade for the test is: A-')

elif n_Average>=87 and n_Average<90:
    print(f'Letter grade for the test is: B+')

elif n_Average>=84 and n_Average<87:
    print(f'Letter grade for the test is: B')

elif n_Average>=80 and n_Average<84:
    print(f'Letter grade for the test is: B-')

elif n_Average>=77 and n_Average<80:
    print(f'Letter grade for the test is: C+')

elif n_Average>=74 and n_Average<77:
    print(f'Letter grade for the test is: C')

elif n_Average>=70 and n_Average<74:
    print(f'Letter grade for the test is: C-')

elif n_Average>=67 and n_Average<70:
    print(f'Letter grade for the test is: D+')

elif n_Average>=64 and n_Average<67:
    print(f'Letter grade for the test is: D')

elif n_Average>=60 and n_Average<64:
    print(f'Letter grade for the test is: D-')

elif n_Average<60:
    print(f'Letter grade for the test is: F')

    
    



    
