import pandas as pd

productData = pd.read_csv("products.csv")

head = productData['Price'].head()
print(head.mean())
avgPrdctPrice = productData['Price'].mean()
print(avgPrdctPrice)
averagePrices = productData.groupby(['ProductName'])['Price'].mean()
averagePrices.plot.bar(figsize=(10,6), color='blue', title='Average Prices Chart')