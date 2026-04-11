import matplotlib.pyplot as plt

# Sample dataset
sizes = [30, 25, 20, 15, 10]
labels = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Sample Pie Chart')
plt.axis('equal')
plt.tight_layout()
plt.show()