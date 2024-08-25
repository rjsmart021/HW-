#Module 2 Lesson 7: Assignments | Python Exception Handling
help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
    'Ten': '10',
    'Thirty': '30',
    'Fourty': '40'
}
#1. Exceptional Weather Forecast
#Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.
# initializing string
# printing result
Fahrenheit_1 = float(input("Temperature in Fahrenheit"))
#Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius.
# Remember that the formula is (Fahrenheit - 32) * 5/9
def Fahrenheit_to_Celsius(Fahrenheit):
    try:
        Celsius = (Fahrenheit - 32)*5/9
        print("The Temperature in Celsius is", Celsius)
    except ValueError:
        print("ValueError")

#Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

while True:
    a = input("Will you be inputing Fahrenheit in 1 .numbers or 2 .Letters?")
    if a == "1":
        Fahrenheit = float(input("Temperature in Fahrenheit"))
        Fahrenheit_to_Celsius(Fahrenheit)         
    elif a == "2":
        F = str(input("The Temperature in Fahrenheit:"))
        res = ''.join(help_dict[ele] for ele in F.split())
        Fahrenheit = F.join(help_dict[ele] for ele in F.split())
        Fahrenheit_to_Celsius(Fahrenheit)
    else:
        print("Select a valid input")
    break
#Task 4: Finally Add a finally block that thanks the user for using the weather forecast application
print("Thank you for using the Whether forecast application!")
#ensuring that this message is displayed regardless of whether an exception was caught or not.
