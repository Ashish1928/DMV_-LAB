def process_data(data):
    x = data.get('x', 0)
    y = data.get('y', 0)

    return x + y

data1 = {'x': 10, 'y': 5}
data2 = {'x': 7}          
data3 = {}               

print(process_data(data1)) 
print(process_data(data2)) 
print(process_data(data3))  
