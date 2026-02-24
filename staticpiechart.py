import matplotlib.pyplot as plt
labels = ['Math', 'Science', 'English']
sizes = [10, 15, 5]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.axis('equal')


plt.title('Favorite Subjects')


plt.show()
