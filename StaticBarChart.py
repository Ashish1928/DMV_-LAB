import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

plt.bar(categories, values, color='skyblue', edgecolor='black')

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Static Bar Chart Example")

plt.show()
