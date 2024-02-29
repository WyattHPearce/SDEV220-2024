import pandas as pd

# Read top 10 rows
df = pd.read_csv('telco_churn.csv')
print(df.head(10))



# Print bottom 5 rows
print(df.tail())



# Convert a dictionary to a dataframe
tempdict: dict = {
    'col1': [1,2,3],
    'col2': [4,5,6],
    'col3': [7,8,9]
}
dictdf: pd.DataFrame = pd.DataFrame.from_dict(tempdict)
print(dictdf.head())



# Print all column names and data types
print(df.columns)
print(df.dtypes)

# Sumary statistics
df.describe(include='object')

# Filtering columns
print(df.State)
print(df["International plan"])
df[['State', 'International plan']]

# Print unique values in a column
print(df.Churn.unique())

# Print rows that match one and multiple columns
print(df[df['International plan']=='No'])
print(df[(df['International plan']=='No') & (df['Churn']==False)])

# Accessing specific rows with iloc
print(df.iloc[14])
# Accessing a specific row AND column
print(df.iloc[14,0])
# iloc with slice to access specific range of rows
print(df.iloc[22:33]) # include, exclude (22, 33)

# Create a copy of my dataframe, then set new index
state = df.copy()
state.set_index('State', inplace=True)
state.head()

# Use lock to find rows that only have OH
print(state.loc['OH'])

# print sum of rows where each column has null
print(df.isnull().sum())
# Drop all null values
df.dropna(inplace=True)
print(df.isnull().sum()) # Display

# Dropping/deleting an entire column
df.drop('Area code', axis=1)

# Creating calculated column
df['Sum Minutes'] = df['Total night minutes'] + df['Total intl minutes']
print(df.head())

# Updating an entire column
df['Sum Minutes'] = 100
# Updating a single column
df.iloc[0,-1] = 10
print(df.head())# Display

# Condition based updating using apply
df['Churn Binary'] = df['Churn'].apply(lambda x: 1 if x==True else 0)
print(df[df['Churn']==True].head())

# Dataframe conversions
df.to_csv('output.csv')
df.to_json('output.json')
df.to_html('output.html')

# delete dataframe
del df