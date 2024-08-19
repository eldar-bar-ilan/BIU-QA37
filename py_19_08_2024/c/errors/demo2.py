def divide(a: float, b: float) -> float:
    if b != 0:
        # if all is good - the method returns
        return a / b
    else:
        # if there is an error - the method throws error (raise)
        error = ArithmeticError('you cannot divide by 0')
        raise error


try:
    print(divide(10, 5))
    print(divide(10, 0))
except ArithmeticError as e:
    # handler code to run in case of error
    print("Error")
# rest of program:
print("Hello - this program is still alive thanks to error handling")
