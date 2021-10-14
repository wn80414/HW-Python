def calculator (number1, number2, operator):
    """
    Calculates the value for an equation with two numbers.

    This function takes an input and calculates the return value of the 
    mathematical operation.

    Parameters
    ----------
    number1 : float
        First number in the equation.
    number2 : float
        Second number in the equation.
    operator : string
        Operator sign of the equation.

    Returns
    -------
    float
        Value after the operation.

    Examples
    --------
    >>> calculator(1, 3, "+")
    4

    >>> calculator(3, 2, "**")
    9
        
    """
    if (number1  == False or number2 == False):    #Checking for valid number
        return False
    if operator == "+":                            #Checking for valid operator
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "/":
        if number2 == 0:
            return False
        return number1 / number2
    elif operator == "*":
        return number1 * number2
    elif operator == "//":
        if number2 == 0:
            return False
        return number1 // number2
    elif operator == "**":
        return number1 ** number2
    else: 
        return False

def parse_input():
    """
    Takes input from the user.

    This function takes input from the user and passes it to the 
    calculator method to be evaluated.
    Equations have to be inputed in a specific format:
    20 + 3
    4 * 11

    This will not work:
    6*3
    2x4
    
    Examples
    --------
    Enter equation: 10 + 11
    
    Enter equation: 3 ** 2
    """
    equation = input("Enter equation: ")
    valu = equation.split(" ")  #Taking a string and spliting it by spaces to create a list with each paramenter having its own element
    num1 = valu[0]              
    num2 = valu[2]
    oper = valu[1]
    if not num1.isdigit(): 
        num1 = False            #Checking if nums are valid digits
    else:                       
        num1 = float(num1)      #Converts from String to Float in order to calculate in the calculator() method

    if not num2.isdigit():
        num2 = False
    else:
        num2 = float(num2)
    print(calculator(num1, num2, oper))
