def checker(function, *args, **kwargs):
    try:
        result = function(*args, **kwargs)
    except Exception as exc:
        print(f"We have problems {exc}")
    else:
        print(f"No problem. Result - {result}")


def calculate(expression):
    return eval(expression)


checker(calculate, "2+2")
