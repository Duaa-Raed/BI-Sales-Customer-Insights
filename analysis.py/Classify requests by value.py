import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



classify_requests_by_value=pd.read_csv('C:/Users/duaar/OneDrive/Desktop/SalesPerformance/Classify requests by value.csv')

classify_requests_by_value.info()
print(classify_requests_by_value.isnull().sum())
print(classify_requests_by_value.head())

print(classify_requests_by_value.describe())
def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    print(f"Number of outliers in {column}: {len(outliers)}")
    return outliers

# Create boxplots for all columns
columns_to_check = classify_requests_by_value.select_dtypes(include=['float64', 'int64']).columns
plt.figure(figsize=(15, 5))

# Check outliers
for column in columns_to_check:
    outliers = detect_outliers_iqr(classify_requests_by_value, column)
    print(f"\nOutliers for {column}:")
    print(outliers)

# Plot boxplots
plt.figure(figsize=(15, 5))
for i, column in enumerate(columns_to_check, 1):
    plt.subplot(1, len(columns_to_check), i)
    sns.boxplot(y=classify_requests_by_value[column])
    plt.title(f'Boxplot of {column}')
plt.tight_layout()
plt.show()

# Save the file to the specified path
import os

# Define the target path
target_path = r'C:\Users\duaar\OneDrive\Desktop\analysis.py'

# Get the current file's content
current_file = __file__

# Copy the current file to the target location
with open(current_file, 'r', encoding='utf-8') as source:
    content = source.read()
    
with open(target_path, 'w', encoding='utf-8') as target:
    target.write(content)

print(f"File has been saved to: {target_path}")
