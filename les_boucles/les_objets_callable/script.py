import random

def is_callable(attr):
    is_callable = callable(getattr(random, attr))
    is_lower = attr.islower()
    is_public = "_" not in attr
    return is_callable and is_lower and is_public

callable_attributes = [x for x in dir(random) if is_callable(x)]
print(callable_attributes)