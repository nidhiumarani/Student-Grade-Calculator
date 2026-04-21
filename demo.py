# printing a line in python
print("Hi Alex! blue is a great colour")

# temperature convertor
def tempConvertor(celcius):
    farenheit = (celcius * (9/5)) + 32
    return farenheit

celciusTemperature = float(input("Please enter temperature in celcius: "))
print(celciusTemperature, "converted to Faranheit becomes", tempConvertor(celciusTemperature))

# Even or odd (asking the user for a number and check if that number is even or odd)
def even_or_odd(num):
    if(num % 2 == 0):
        return "even number"
    else:
        return "odd number"
    
input_number = int(input("Please enter a number to check it is even or odd: "))
print("The entered number", input_number, "is", even_or_odd(input_number))

# word reverser
input_string = input("Please enter a string and the output will be reverse of that string")


