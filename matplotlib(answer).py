Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #  When we use py gradle, this is what it would look like
... #  Load and Explore the Dataset  
... import pandas as pd  
... import matplotlib.pyplot as plt  
... import seaborn as sns  
... 
... # Load the Iris dataset  
... url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"  
... column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']  
... try:  
...     iris_data = pd.read_csv(url, header=None, names=column_names)  
... except FileNotFoundError:  
...     print("File not found. Please check the URL.")  
... 
... # Display the first few rows  
... print(iris_data.head())  
... 
... # Explore the structure of the dataset  
... print(iris_data.info())  
... print(iris_data.isnull().sum())  # Check for missing values  
... 
... # Clean the dataset (no missing values in the Iris dataset)  
... # If there were missing values, you could drop or fill them  
... # iris_data.dropna(inplace=True)  # Example of dropping missing values  
... 
... # Basic Data Analysis  
... # Descriptive statistics  
... print(iris_data.describe())  
... 
... # Grouping by species and computing the mean of petal length  
... mean_petal_length = iris_data.groupby('species')['petal_length'].mean()  
... print(mean_petal_length)  
... 
... # Step 3: Data Visualization  
... # Set the aesthetic style of the plots  
sns.set(style="whitegrid")  

# Line chart (not applicable for this dataset, but we can create a plot for demonstration)  
# For demonstration, let's create a bar chart instead  
plt.figure(figsize=(10, 6))  
mean_petal_length.plot(kind='bar', color='skyblue')  
plt.title('Average Petal Length by Species')  
plt.xlabel('Species')  
plt.ylabel('Average Petal Length (cm)')  
plt.xticks(rotation=45)  
plt.legend(['Mean Petal Length'])  
plt.show()  

# Histogram of petal length  
plt.figure(figsize=(10, 6))  
sns.histplot(iris_data['petal_length'], bins=10, kde=True, color='purple')  
plt.title('Distribution of Petal Length')  
plt.xlabel('Petal Length (cm)')  
plt.ylabel('Frequency')  
plt.show()  

# Scatter plot of sepal length vs petal length  
plt.figure(figsize=(10, 6))  
sns.scatterplot(data=iris_data, x='sepal_length', y='petal_length', hue='species', style='species', s=100)  
plt.title('Sepal Length vs Petal Length')  
plt.xlabel('Sepal Length (cm)')  
plt.ylabel('Petal Length (cm)')  
plt.legend()  
