try:
    print("Start code")
    print(10/0)
    print("No error")
except (NameError, ZeroDivisionError):
    print("We have error")
    print("На 0 ділити не можна")
print("End program")
