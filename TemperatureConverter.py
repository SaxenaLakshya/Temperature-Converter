print("Welcome to Temperature Converter.....")
def TemperatureConverter():
    print("""Please tell what is the Temperature you have got?
    Please enter the corresponding number of the Scale you have got
    1. If you have got Celsius Scale
    2. If you have got Fahrenheit
    3. If you have got Kelvin""")
    temp_type = int(input("Enter the Corresponding Number: "))
    if temp_type == 1:
        temp_unit = int(input("Enter the Temperature Unit: "))
        print(f"The Temperature is {temp_unit} degree Celsius")
        print("""Please enter the corresponding number of the Temperature to which you want to convert
        1. If you want Celsius to Fahrenheit
        2. If you want Celsius to Kelvin""")
        converter = int(input("Enter the corresponding number: "))
        if converter == 1:
            print((temp_unit * 9/5) + 32, " Fahrenheit")
        elif converter == 2:
            print(temp_unit + 273.15, " Kelvin")
        else: print("Please run the code again and enter the correct inputs")
    elif temp_type == 2:
        temp_unit = int(input("Enter the Temperature Unit: "))
        print(f"The Temperature is {temp_unit} Fahrenheit")
        print("""Please enter the corresponding number of the Temperature to which you want to convert
                1. If you want Fahrenheit to Celsius
                2. If you want Fahrenheit to Kelvin""")
        converter = int(input("Enter the corresponding number: "))
        if converter == 1:
            print((temp_unit - 32) * 5/9, " degree Celsius")
        elif converter == 2:
            print((temp_unit - 32) * 5/9 + 273.15, " Kelvin")
        else: print("Please run the code again and enter the correct inputs")
    elif temp_type == 3:
        temp_unit = int(input("Enter the Temperature Unit: "))
        print(f"The Temperature is {temp_unit} Kelvin")
        print("""Please enter the corresponding number of the Temperature to which you want to convert
                1. If you want Kelvin to Celsius
                2. If you want Kelvin to Fahrenheit""")
        converter = int(input("Enter the corresponding number: "))
        if converter == 1:
            print(temp_unit - 273.15, " degree Celsius")
        elif converter == 2:
            print((K - 273.15) * 9/5 + 32, " Fahrenheit")
        else: print("Please run the code again and enter the correct inputs")
    else:
        print("Please enter the correct option!")
