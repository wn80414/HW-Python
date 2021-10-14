def tripler(func):
    """
    A decorator that runs a func three times.
    
    Parameter
    ---------
    func : a function

    Example
    -------
    >>> tripler(print("Hey"))
    Hey
    Hey
    Hey
    """
    def wrapper():
        func()
        func()
        func()
    return wrapper
