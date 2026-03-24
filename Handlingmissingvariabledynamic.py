def process_data(data):
    # Safely access dynamic variables with defaults
    x = data.get('x', 0)
    y = data.get('y', 0)

    return x + y

# Example inputs (dynamic)
data1 = {'x': 10, 'y': 5}
data2 = {'x': 7}          # 'y' is missing
data3 = {}                # both missing

print(process_data(data1))  # 15
print(process_data(data2))  # 7
print(process_data(data3))  # 0