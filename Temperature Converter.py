#Displays my name, states its purpose, asks for temperature input
f_Temperature=float(input(f"Welcome! Thank you for using Patrick's temperature converter. Please enter a temperature: "))

#Asks user for specification on Celsius or Farenheit
str_FarenheitOrCelsius=str(input(f'Please enter whether your temperature was in Farenheit "F", or Celsius "C": '))


#Decides if input for "str_FarenheitOrCelsius" ended up being Farenheit. If so, it determines if initial temperature is at or below 212.
#Converts Farenheit to Celsius and displays conversion to user. If initial temperature is above 212, display message to user.

if str_FarenheitOrCelsius.upper()=='F':
    if f_Temperature<=212:
        f_ConvertedTemperature=float((5.0/9)*(f_Temperature-32))
        print(f'The Celsius equivalent is: {f_ConvertedTemperature:.1f}')
    else:
        print(f'Temp can not be > 212.')



#Decides if input for "str_FarenheitOrCelsius" ended up being Celsius. If so, it would determine if the intial temperature is at or below 100.
#Converts Celsius to Farenheit and displays conversion to user. If initial temperature is above 100, display message to user.
        
elif str_FarenheitOrCelsius.upper()=='C':
    if f_Temperature<=100:
        f_ConvertedTemperature=float(((9.0/5.0)*f_Temperature+32))
        print(f'The Farenheit equivalent is: {f_ConvertedTemperature:.1f}')
    else:
        print(f'Temp can not be > 100.')


#If "str_FarenheitOrCelsius" was not given an F or a C for its input, it will display the message below.
        
else:
    print('You must enter an F or a C.')
    
    













