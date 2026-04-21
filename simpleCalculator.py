# Simple calculator
def addition(input1, input2): return input1 + input2
def substraction(input1, input2): return input1 - input2
def multiplication(input1, input2): return input1 * input2
def division(input1, input2): return input1 % input2

input1, input2 = map(int, input("Please enter 2 numbers for Math opeerations: ").split())
print("Please select any of the choice")
choice = input("1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Division \n")
if(choice == "1"):
    print("Addition of 2 numbers is:", addition(input1, input2))
elif(choice == "2"):
    print("Substraction of 2 numbers is:", substraction(input1, input2))
elif(choice == "3"):
    print("Multiplication of 3 numbers is:", multiplication(input1, input2))
else:
    print("Division of 2 numbers is:", division(input1, input2))