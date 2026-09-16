def divide_numbers(a, b):
    try:
        print("Attempting division...")
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Both inputs must be numbers.")
    else:
        print(f"Success! The result is {result}")
    finally:
        print("Division operation finished.\n")

# Test 1: valid input (Triggers try, else, finally)
divide_numbers(10, 2)

# Test 2: math error (Triggers try, except ZeroDivisionError, finally)
divide_numbers(10, 0)

# Test 3: type error (Triggers try, except TypeError, finally)
divide_numbers(10, "a")