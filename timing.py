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
    current_time = time.time()
    func
    after_time = time.time()
    run_time = after_time - current_time  #Finds the difference between current_time and after_time to find total run time
    print("Total time", run_time)



