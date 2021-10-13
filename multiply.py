def multiply_list(listParam):
    '''
    Multiply elements in a list.
    
    This function multiplies all of the elements in a list to get a product.
    The function can only multiply ints and floats.
    It returns false if there is an invalid item inside the list or if
    it is empty.
    
    Parameters
    ----------
    list : list
        List with elements to be multiplied. 

    Examples
    --------
    list = [1, 2 ,3 ,4 ,5]
    >>> multiply_list(listParam)
    120
    
    list = []
    >>> multiply_list(listParam)
    false
    
    list = ["null", 2, 5 ,2]
    >>> multiply_list(listParam)
    false
    '''
    total = 1                   #Starts with a value of 1
    if len(listParam) == 0:  
        return False            #Returns false if array is empty
    for num in listParam:           
        #Checks for valid input
        if isinstance(num, int) or isinstance(num, float):
            total = num * total
        else:
            return False
    return total
