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

** High-Value Customers Analysis*
----
*Business Questions*

Who are the most valuable customers in terms of total spending?

Are there any unusual high spenders or inconsistent order behavior?

How can we categorize customers based on their spending?

*Summary*

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

Cleaned using pandas: verified datatypes, checked for nulls, and preserved all valid outliers.

Applied segmentation logic:

High Roller (> 450,000 in spending)

Loyal Customer (> 150,000)

Regular Customer (others)

Dataset is ready for dashboard visualization in Power BI.

📂 File:

High-Value Customers.csv

✅ More analysis summaries will be added below as they are completed.

🧠 Tools Used

SQL (Data extraction from AdventureWorks)

Python (pandas, seaborn, matplotlib) (Data wrangling & exploration)

Power BI (Visualization & dashboarding)

📝 Author

Duaa Raed — Data Analyst | SQL | Python | Power BI

