import pandas as pd
import matplotlib.pyplot as  plt
import seaborn as sns


high_Value_Customers=pd.read_csv('C:/Users/duaar/OneDrive/Desktop/SalesPerformance/High-Value Customers.csv')

high_Value_Customers.info()
print(high_Value_Customers.isnull().sum())
print(high_Value_Customers.head())


print(high_Value_Customers.describe())
print("-------------")
def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    print(f"عدد القيم المتطرفة في {column}: {len(outliers)}")
    return outliers

# Create boxplots for all three columns
columns_to_check = ['TotalSpent', 'OrdersCount', 'AvgOrderValue']
plt.figure(figsize=(15, 5))

# فحص القيم المتطرفة
for column in columns_to_check:
    outliers = detect_outliers_iqr(high_Value_Customers, column)
    print(f"\nOutliers for {column}:")
    print(outliers)

# ------------------------
#  إضافة التصنيف بعد التأكد من القيم المتطرفة
def classify_customer(spent):
    if spent > 450000:
        return 'High Roller'
    elif spent > 150000:
        return 'Loyal Customer'
    else:
        return 'Regular Customer'

high_Value_Customers['CustomerSegment'] = high_Value_Customers['TotalSpent'].apply(classify_customer)

# عرض التوزيع
segment_counts = high_Value_Customers['CustomerSegment'].value_counts()
print("\nCustomer Distribution by Classification:")
print(segment_counts)

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
