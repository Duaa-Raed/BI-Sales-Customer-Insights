------
Sales Performance Analysis Dashboard
-----

---
**Project Overview**

This project aims to analyze and visualize key sales and customer performance indicators extracted from the AdventureWorks database using SQL and Python. The data was prepared for advanced business intelligence visualization using Power BI.

All datasets were retrieved directly from the AdventureWorks relational database and exported as CSV files for data cleaning, feature engineering, and analysis.

The project includes multiple analytical modules, each designed to answer specific business questions using cleaned and enriched data.

---
**Extracted Datasets**

High-Value Customers.csv

Monthly Sales Change Analysis.csv

Classify Requests by Value.csv

Top 5 Best-Selling Products in Each Country.csv

-------

High-Value Customers Analysis
----
**Business Questions**

- Who are the most valuable customers in terms of total spending?

- Are there any unusual high spenders or inconsistent order behavior?

- How can we categorize customers based on their spending?

**Data Source and Extraction**

Extracted from AdventureWorks using a SQL query that joins customer and sales order data.

```sql
SELECT 
    c.CustomerID,
    ISNULL(per.FirstName + ' ' + per.LastName, 'Store Account') AS CustomerName,
    SUM(sod.OrderQty * sod.UnitPrice) AS TotalSpent,
    COUNT(DISTINCT soh.SalesOrderID) AS OrdersCount,
    AVG(sod.OrderQty * sod.UnitPrice) AS AvgOrderValue
FROM Sales.SalesOrderHeader AS soh
JOIN Sales.SalesOrderDetail AS sod ON soh.SalesOrderID = sod.SalesOrderID
LEFT JOIN Sales.Customer AS c ON soh.CustomerID = c.CustomerID
LEFT JOIN Person.Person AS per ON c.PersonID = per.BusinessEntityID
GROUP BY c.CustomerID, per.FirstName, per.LastName
HAVING SUM(sod.OrderQty * sod.UnitPrice) > 10000
ORDER BY TotalSpent DESC;
```

**Data Cleaning**

Verified data types and ensured there are no missing values.

Outliers were examined and retained, as they represent significant high-value customers.

**Customer Segmentation**

*Based on total spending, customers were segmented as follows:*

- High Roller: Customers spending more than 450,000

- Loyal Customer: Customers spending between 150,000 and 450,000

- Regular Customer: Customers spending less than or equal to 150,000

*The distribution of customers across segments is:*

- Regular Customer: 297

- Loyal Customer: 143

- High Roller: 38

**Summary and Next Steps**

Identified the most valuable customers and categorized them into clear spending segments.

Noted the presence of high-spending customers (outliers) which may warrant further behavioral analysis.

The cleaned and segmented data is now ready for visualization and dashboard creation in Power BI.

-----

Classify requests by value
----
**Business Questions**

- Are there any extreme or unusual values in the TotalDue column?

- How many outliers exist in the dataset and what categories do they belong to?

- Should these outliers be removed or retained for further analysis?

**Data Source and Extraction**

Extracted from AdventureWorks using a SQL query that joins customer and sales order data.

```sql
SELECT 
    soh.SalesOrderID,
    soh.TotalDue,
    CASE 
        WHEN soh.TotalDue >= 10000 THEN 'High'
        WHEN soh.TotalDue >= 5000 THEN 'Medium'
        ELSE 'Low'
    END AS OrderCategory
FROM Sales.SalesOrderHeader AS soh
ORDER BY soh.TotalDue DESC;
```

**Data Cleaning**

- Data types were verified and no missing values were found.

- Outliers were reviewed and retained because they represent significant transactions.

*Outliers Detection*

- No outliers found in SalesOrderID.

- 2,127 outliers detected in TotalDue.

*Reason for Retaining Outliers*

The identified outliers in the TotalDue column represent significant transactions that are important from a business perspective. These high-value orders are not errors or data anomalies but rather reflect real customer behaviors, such as large or bulk purchases. Removing them could lead to loss of valuable insights about key customer segments and spending patterns. Therefore, they are retained to ensure a comprehensive and accurate analysis of sales performance.*

**Summary and Next Steps**


Confirmed presence of high-value and medium-value outliers in TotalDue.

Decided to keep these outliers for comprehensive analysis to better understand customer spending behavior.

Data is now prepared for further visualization and advanced analytics in Power BI.








