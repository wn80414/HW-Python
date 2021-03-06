def multiply_list(listParam):
    '''
    Multiply elements in a list.
    
    This function multiplies all of the elements in a list to get a product.
    The function can only multiply ints.
    It returns false if there is an invalid item inside the list or if
    it is empty.
    
    Parameters
    ----------
    list : list
        List with elements to be multiplied.

    Returns
    -------
    int 
        Product of all elements in the list.

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
    total = 1                   #Starts with a value of 1 so when the first element is multiplied the total will = first element
    if len(listParam) == 0:  
        return False            #Return false if array is empty because you can not multiply nothing
    for num in listParam:            
        if isinstance(num, int):  #Checking for valid elements
            total = num * total
        else:
            return False
    return total
