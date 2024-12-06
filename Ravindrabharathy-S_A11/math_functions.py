def power(base, exponent):
    try:
        return base ** exponent
    except Exception as e:
        return f"Error: {e}"

def divide(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."
    except Exception as e:
        return f"Error: {e}"
