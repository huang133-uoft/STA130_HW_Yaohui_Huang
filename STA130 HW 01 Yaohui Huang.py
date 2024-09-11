#!/usr/bin/env python
# coding: utf-8

# #### Question 1

# In[1]:


import pandas as pd

# Define the column names, since the dataset does not have headers
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
    'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
    'hours_per_week', 'native_country', 'income'
]

# Import the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
df = pd.read_csv(url, header=None, names=column_names, na_values=' ?')

# Display the first few rows of the dataset
print(df.head())

# Check for missing values in each column
missing_values = df.isnull().sum()

# Display the columns with missing values and their counts
print(missing_values)


# #### Question 2.1

# In[3]:


import pandas as pd

# Load the dataset
column_names = [
    "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
    "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
    "hours-per-week", "native-country", "income"
]

# Replace 'adult.data' with the path to your downloaded file if necessary
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
df = pd.read_csv(url, names=column_names, na_values=' ?', sep=',', skipinitialspace=True)

# Display the number of rows and columns
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")


# Question 2.2

# Observations are specific data collected from observational units, which can be understand as a actual value for 'varaibles', and every individual obervation corresponds to a row in a tabular dataset.
# 
# Variables stand for the groups of quantities or characteristics that can be measured and recorded. Variables can assumed by more than one value from observations, every variable corresponds to a column in a tabular dataset.  

# #### Question 3

# In[10]:


import pandas as pd

# Load the dataset
column_names = [
    "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
    "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
    "hours-per-week", "native-country", "income"
]
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
df = pd.read_csv(url, names=column_names, na_values=' ?', sep=',', skipinitialspace=True)

# Overview of dataset
print("Dataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics (Numerical):")
print(df.describe())

# Summary statistics for all columns
print("\nSummary Statistics (All Columns):")
print(df.describe(include='all'))

# Frequency counts for a specific column
print("\nValue Counts for 'education':")
print(df['education'].value_counts())

# Missing values
print("\nMissing Values in Each Column:")
print(df.isna().sum())

# Number of unique values
print("\nUnique Values in Each Column:")
print(df.nunique())


# #### Question 4

# In[5]:


import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Check the shape of the DataFrame
print(df.shape)

# Summary statistics of numeric columns
print(df.describe())

print(df.describe(include='all'))


# (a)
# The reason that the columns analyzed by df.describe() is much more fewer than the actual number of columns is becuase df.describe only summarizes numerical columns by default. When analyzing a dataset containing categorical columns, the categorical columns won't appear in the summary unless you specify "include='all'".
# 
# (b)
# The reason for this discrepancy is due to missing values. The "count" column for the output of df.describe() represents the number of non-missing values for each columns. Therefore, whenever a column exist missing values, the "count" will deduct this value from the total number of rows in the Dataframe, which causes the discrepancy for the values reported.
# 

# #### Question 5

# Attributes is a variable representing the proerties of an object that comes without parentheses. It provides a direct access to data and usually used to get or set values (for example: number of columns) that does not require any computation process.
# 
# Method is a funcion to execute that comes with parentheses. It performs a action that may returns a result such as processing the data, which requires some level of processing and compution.

# #### Question 6

# Count: The number of non-null(NaN excluded) values in the column.
# 
# Mean: Sum of all the values divided by "count", which represents the avaerage value of the column. (central trendency)
# 
# STD: Standard deviation is 'the quare root of the average of the squared differences between each value and the mean', which is a measure of the dispersion or spread of the values in the column.
# 
# Min: Minimum is the smallest value in the column.
# 
# 25%: The value below which 25% of the data points fall, also known as Q1.(25% values lie under this line)
# 
# 50%: Median is the middle value of the column when all values are sorted in ascending order.
# 
# 75%: The value below which 75% of the data points fall, also known as Q3.
# 
# Max: Maximum is the greatest value in the column.

# #### Question 7

# (a)
# df.dropna() is perferred when you want to analyze only the complete data, since it helps to remove rows or colomns with missing value.
# 
# (b)
# In contrast, del df['col'] is perferred when you want to remove an entire column from the dataFrame, which might cause the lost of potentially valuable data.
# 
# (c)
# There are three main reasons make it important to apply del df['col'] first, including prevent the loss of useful data in rows, reduce the stress of analysis by reduing the size of the DataFrame and also helps maintain a better data proprocessing logic.
# 
# (d)
# This is a combination of two df.dropna. The first step is applied todrop columns with sinificant missing data more than 30% in order to retain the informative parts of the dataset. The second step is used to drop rows with remaining missing data from the first setp, which ensures the dataset is clean for analyze. Before cleaning the dataset, the data shape is (891, 15); and after the cleaning, the data shape remians (712, 14). 

# In[4]:


import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Before: Check the number of missing values in each column
missing_data_before = df.isna().sum()
print("Missing data (before):")
print(missing_data_before)

# Step 1: Drop columns with more than 30% missing values
threshold = len(df) * 0.3
df = df.dropna(thresh=threshold, axis=1)

# Step 2: Drop rows with any remaining missing values
df_cleaned = df.dropna()

# After: Check the number of missing values in each column
missing_data_after = df_cleaned.isna().sum()
print("\nMissing data (after):")
print(missing_data_after)

# Before and after shape comparison
print("\nData shape before cleaning:", (891, 15))
print("Data shape after cleaning:", df_cleaned.shape)


# #### Question 8.1

# In[5]:


import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)


print(df.head())


result = df.groupby("embark_town")["age"].describe()
print(result)


# #### Question 8.2

# First, df.describe() provides data for the entire column across all rows, which df.groupby("col1")["col2"].describe()for a column whthin groups defined by another column. Secondly, df.describe() shows all non-null values in the dataset. Thirdly, df.groupby("col1")["col2"].describe() helps processing data with specific subsets rather than df.describe()provides a overall sense of the dataset.

# #### Question 8.3

# ChatBots such as Chatgpt are much more reliable on fixing error when coding comparing to Google search. Their advantage is to analyze the specific codes we are dealing with and give instructions in direct and precise ways immediately. The biggest problem of using Google search is it always give a long-winded expalinanation, and it's much more inefficient.
# 
# 
# A. 
# Both Chatgpt and Google search gives the troubleshooting help quickly and precisely. Since the Chatbot gives the fixed coding direclty, it solves this error more quickly. 
# 
# B. 
# Both Chatgpt and Google search finds the error and gives the instruction of cheking the URL at the first time.
# 
# C. 
# Google gives the troubleshoot slower that Chatgpt. Chatgpt gives the instruction to check variable definition at the very beginning but Google does not.
# 
# D. 
# Both Chatgpt and Google gives the right insturction, but Chatgpt is much more quickly and direclty.
# 
# E.
# Chatgpt solves the error directly but Google does not provide the right method.
# 
# F.
# Chatgpt gives the solution at the first step, and Google's answers are much more complex.
# 
# G.
# Chatgpt gives instruction which are more clearly to fix this error.

# #### Question 9

# Yes. I did review those materials, but is doesn't helps that much to understand quckily, since I have no former experiences or knowledges with related contents.

# #### Chatlog history

# https://chatgpt.com/share/06e5e524-267a-45ce-8dd3-498efde8c859
# 
# Summary:
# 
# 1. Dataset Introduction:
# Adult (Census Income) Dataset: A dataset from the UCI Machine Learning Repository used for predicting income levels based on various demographic and economic attributes. It contains 48,842 records and 14 attributes.
# 2. Determining Dataset Dimensions:
# To find the number of rows and columns in a pandas DataFrame, use df.shape which returns a tuple (rows, columns).                 
# 3. Observation in the Dataset:
# An observation is a single individual's record, including various attributes like age, workclass, and income level.
# 4. Variable in the Dataset:
# A variable (or feature) represents a specific characteristic of the data. In the Adult dataset, examples include age, workclass, education, and income.
# 5. Summarizing Dataset Columns:
# df.describe(): Provides a summary of numerical columns (mean, standard deviation, min, max).                   
# df.describe(include='object'): Summarizes categorical columns (unique values, top category, frequency).        
# df.info(): Gives data types and missing values.                                                               
# df.value_counts(): Shows frequency of categories in a specific column.                                        
# df.nunique(): Shows the number of unique values in each column.                                              
# df.agg(): Allows for custom aggregations.
# 

# https://chatgpt.com/share/6468a503-bd4b-44c6-9026-35a37f9d6a85 
# 
# The chat discusses why there is a difference between the dataset size shown by `df.shape` and the columns analyzed by `df.describe()`. The reason is that `df.describe()` only includes numeric columns by default, excluding non-numeric ones.
# Next, a method to remove missing data from the Titanic dataset is provided: first, drop columns with a high percentage of missing values, then drop any remaining rows with missing data. This approach helps ensure a clean dataset for analysis. The explanation includes the steps and rationale, though executing the code was not possible due to a network issue.

# https://chatgpt.com/share/672a5d12-499f-462d-935e-0abb54300bc1
# 
# Summary:
# 
# 1. Overview of the Dataset:                                                                         
# Dataset URL: Adult Income Dataset                                                                      
# The dataset contains demographic information and income levels.                                            
# 2. Key Concepts:
# Attributes vs. Methods:                                                                                         
# Attributes (e.g., df.shape): Variables that provide information about the object without parentheses.         
# Methods (e.g., df.describe()): Functions that perform actions on the object and require parentheses to call.   
# Summary Statistics in df.describe():                                                                          
# Count: Number of non-null entries.                          
# Mean: Average value.                                                                       
# Standard Deviation (std): Measure of dispersion. 
# Min: Smallest value.                                                                     
# 25%: 25th percentile value.                                               
# 50% (Median): Middle value.                                                                                   
# 75%: 75th percentile value.                                                                                    
# Max: Largest value.                                                                                     
# 3. Handling Missing Data: 
# df.dropna(): Removes rows (or columns) with missing values.                                                    
# del df['col']: Deletes entire columns.           
# 4. Example Approach to Cleaning Data: 
# Step 1: Load the dataset and identify missing values.                                                      
# Step 2: Remove columns with excessive missing values.                                                       
# Step 3: Use df.dropna() to remove rows with any remaining missing values.                                   
# Step 4: Report the shape and missing values before and after cleaning.                                       
# 5. Justification: 
# Using del df['col']: Preferred for removing columns with too many missing values to retain valuable data.      
# Using df.dropna(): Ensures that the remaining rows are complete, suitable for analysis without missing data issues.  
# 6. Example Results: 
# Before Cleaning: The dataset had missing values in several columns.                                            
# After Cleaning: The dataset had no missing values, with changes in the shape of the DataFrame reflecting the removal of incomplete rows or columns. 

# https://chatgpt.com/share/014118a8-736a-42c6-b2c2-2fab88c3b2d7
# 
# Summary:
# 
# 1. df.dropna() vs. del df['col']:                                                   
# df.dropna(): Removes rows with missing values.
# del df['col']: Deletes a specific column.
# 2. Combining Both:
# Deleting a column before removing rows can be useful if the column has many missing values.               
# df.groupby("col1")["col2"].describe():
# Groups data by col1 and provides statistics for col2 within each group.
# 3. Error Handling:
# NameError: Check if the variable is defined and correctly named.                       
# HTTPError 404: Verify the URL or try a different source.                       
# SyntaxError: Check for unclosed parentheses.                             
# AttributeError: Use the correct method name, describe.                               
# KeyError: Ensure the column name exists and is correctly spelled.                   
# NameError for column: Use column names as strings, not variables.                 
# 

# In[ ]:




