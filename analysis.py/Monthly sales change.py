import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

monthly_sales_change_analysis=pd.read_csv('C:/Users/duaar/OneDrive/Desktop/SalesPerformance/Monthly sales change analysis.csv')

monthly_sales_change_analysis.info()
print(monthly_sales_change_analysis.isnull().sum())
print(monthly_sales_change_analysis.head())

print(monthly_sales_change_analysis.describe())
def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    print(f"Number of outliers in {column}: {len(outliers)}")
    return outliers

# Create boxplots for all numeric columns
columns_to_check = monthly_sales_change_analysis.select_dtypes(include=['float64', 'int64']).columns
plt.figure(figsize=(15, 5))

# Check outliers
for column in columns_to_check:
    outliers = detect_outliers_iqr(monthly_sales_change_analysis, column)
    print(f"\nOutliers for {column}:")
    print(outliers)

# Plot boxplots
plt.figure(figsize=(15, 5))
for i, column in enumerate(columns_to_check, 1):
    plt.subplot(1, len(columns_to_check), i)
    sns.boxplot(y=monthly_sales_change_analysis[column])
    plt.title(f'Boxplot of {column}')
plt.tight_layout()
plt.show()
