import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("orders.csv", sep=",")

grouped_data = df.groupby('Dish Name')['Quantity'].sum()

grouped_data.plot(kind = 'bar')
plt.xlabel('Dish Name', fontsize=14)
plt.xticks(rotation=10, fontsize=14) 
plt.ylabel('Quantity Sold', fontsize=14)
plt.title('Total Selling Quantity for Each Dish', fontsize=18)
plt.savefig('selling_quantity_dish.png')
plt.show()

grouped_data = df.groupby('Dish Name')['Selling($)'].sum()

grouped_data.plot(kind = 'bar')
plt.xlabel('Dish Name', fontsize=14)
plt.xticks(rotation=10, fontsize=14) 
plt.ylabel('Total Selling ($)', fontsize=14)
plt.title('Total Selling ($) for Each Dish', fontsize=18)
plt.savefig('selling_dollars_dish.png')
plt.show()
