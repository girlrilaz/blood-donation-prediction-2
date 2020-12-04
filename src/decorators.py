import inspect

def pure(function):
    source = inspect.getsource(function)
    for non_pure_indicator in ('random', 'time', 'input', 'print', 'global'):
        if non_pure_indicator in source:
            raise ValueError("The function {} is not pure as it uses `{}`".format(
                function.__name__, non_pure_indicator))
    return function