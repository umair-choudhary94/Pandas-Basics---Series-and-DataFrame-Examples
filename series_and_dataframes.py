import pandas as pd

# Creating a Pandas Series from a list 'x'
x = [3, 4, 6, 7, 7, 4]
y = pd.Series(x)
print(y)         # Display the Series 'y'
print(type(y))   # Display the type of 'y', which should be a Pandas Series
print(y[5])      # Access the value at index 5 of the Series 'y'

# Changing the index of the Series
x = [3, 4, 6]
y = pd.Series(x, index=["a", "b", "c"])
print(y)         # Display the Series 'y' with new index
print(type(y))   # Display the type of 'y'
print(y["c"])    # Access the value with index "c"

# Giving the Series a name
y = pd.Series(x, index=["a", "b", "c"], name="First data")
print(y)

# Changing the datatype of the Series
y = pd.Series(x, index=["a", "b", "c"], name="Second data", dtype="float")
print(y)

# Creating a Series from a dictionary
x = {"name": ["Python", "Java", "Ruby"], "Rank": [1, 2, 3]}
y = pd.Series(x)
print(y)

# Performing addition on two Series
a = pd.Series(12, index=[1, 2, 3, 4, 5, 6])
b = pd.Series(12, index=[1, 2, 3, 4])
print(a + b)

# Creating a DataFrame from a dictionary
c = {"Name": ["Umair", "Alishba"], "Relation": ["Teacher", "Student"]}
result = pd.DataFrame(c, columns=["Name"], index=["A", "B"])
print(result)

# Accessing a specific element in the DataFrame
print(result["Name"]["B"])

# Creating a DataFrame from a list of lists
c = [[1, 2, 3, 4], [5, 6, 7, 8]]
result = pd.DataFrame(c)
print(result)

# Creating a DataFrame from a dictionary of Series
c = {"Name": pd.Series(["Umair", "Alishba"]), "Relation": pd.Series(["Teacher", "Student"])}
result = pd.DataFrame(c)
print(result)
