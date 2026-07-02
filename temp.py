import pandas as pd
data = {'Name': ['sakshi','gayu','masane'], 'Age': [28, 32, 26],
'City': ['Kolkata', 'Chennai', 'Hyderabad']} 
df = pd.DataFrame(data) 
print("DataFrame:\n", df)
print("Mean Age:", df['Age'].mean()) 
print("DataFrame Description:\n", df.describe())
