def get_value(var_name, default=0):
    try:
        return globals()[var_name]
    except KeyError:
        return default

# Example usage
x = 10  # comment this line to simulate "missing variable"

value = get_value('x')
print(f"Value of x: {value}")