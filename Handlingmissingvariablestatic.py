def get_value(var_name, default=0):
    try:
        return globals()[var_name]
    except KeyError:
        return default

x = 10 

value = get_value('x')
print(f"Value of x: {value}")
