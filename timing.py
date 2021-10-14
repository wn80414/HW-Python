import time
def calculate_time(func):
    """
    Decorator that calculates the run time of a function.

    This decorator finds the total run time of a function and expresses it in seconds.

    Parameters
    ----------
    func : a function

    Examples
    --------
    >>> calculate_time(time.sleep(2))
    Total time 1.1920928955078125e-06
    """
    def wrapper():
        currentTime = time.time()
        funcValue = func()                 
        afterTime = time.time()
        runTime = afterTime - currentTime  #Finds the difference between currentTime and afterTime to find total run time
        print("Total time", runTime)
        return funcValue
    return wrapper



