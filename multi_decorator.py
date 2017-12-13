def existence_checker(func):
    print('calling @existence_checker')
    def wrapper(*args, **kwargs):
        if any([kwargs[kwarg] is None for kwarg in kwargs]):
            print('RAISE manca dato')
        else:
            print('run function, @existence_checker')
            return func(*args, **kwargs)
    return wrapper

def positive_checker(func):
    print('calling @positive_checker')
    def wrapper(*args, **kwargs):
        if any([kwargs[kwarg] < 0 for kwarg in kwargs]):
            print('RAISE valori negativi')
        else:
            print('run function, @positive_checker')
            return func(*args, **kwargs)
    return wrapper


@existence_checker
@positive_checker
def adder(a, b):
    return a + b

    
if __name__ == '__main__':
    # a = 3
    a = None
    b=2
    res = adder(a=a, b=b)
    print(res)