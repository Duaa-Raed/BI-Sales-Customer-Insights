------
Sales Performance Analysis Dashboard
-----
------
**Table of Contents**

- [Project Description](#project-description)
- [High-Value Customers Analysis](#high-value-customers-analysis)
- [Classify Requests by Value](#classify-requests-by-value)
- [Monthly Sales Change Analysis](#monthly-sales-change-analysis)
- [Best-Selling Product Rankings by Country](#best-selling-product-rankings-by-country)
-------
## Project Description

This project presents a comprehensive sales and customer performance analysis using data extracted from the AdventureWorks relational database. The objective is to answer key business questions using SQL for data extraction, Python for cleaning and analysis, and Power BI for visualization.

The analysis covers various dimensions such as:

- Identifying high-value customers.

- Understanding monthly sales trends and growth patterns.

- Classifying sales orders by value.

- Ranking best-selling products by country.

- The cleaned and enriched datasets support strategic decision-making and can be used in interactive dashboards for business insights.




## High-Value Customers Analysis
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



## Classify requests by value
----

**Data Quality Assessment**

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

**Outliers Detection**

- No outliers found in SalesOrderID.

- 2,127 outliers detected in TotalDue.

*Reason for Retaining Outliers*

The identified outliers in the TotalDue column represent significant transactions that are important from a business perspective. These high-value orders are not errors or data anomalies but rather reflect real customer behaviors, such as large or bulk purchases. Removing them could lead to loss of valuable insights about key customer segments and spending patterns. Therefore, they are retained to ensure a comprehensive and accurate analysis of sales performance.

**Summary and Next Steps**


Confirmed presence of high-value and medium-value outliers in TotalDue.

Decided to keep these outliers for comprehensive analysis to better understand customer spending behavior.

Data is now prepared for further visualization and advanced analytics in Power BI.



## Monthly_sales_change_analysis
---

**Business Questions**

- How are monthly sales trending over time?

- Are there months with unusually high or low sales growth?

- What is the average monthly growth rate, and how volatile is it?


**Data Source and Extraction**

The data was extracted from the Sales.SalesOrderHeader and Sales.SalesOrderDetail tables in the AdventureWorks database.
Monthly total sales were calculated by aggregating the product of order quantity and unit price, grouped by the order date formatted as year and month (yyyy-MM).
A Common Table Expression (CTE) was used to first calculate monthly total sales. Then, the sales growth rate was computed by comparing each month’s total to the previous month using the LAG() window function.

```sql
WITH MonthlySales AS (
    SELECT 
        FORMAT(soh.OrderDate, 'yyyy-MM') AS SaleMonth,
        SUM(sod.OrderQty * sod.UnitPrice) AS TotalSales
    FROM Sales.SalesOrderHeader AS soh
    JOIN Sales.SalesOrderDetail AS sod ON soh.SalesOrderID = sod.SalesOrderID
    GROUP BY FORMAT(soh.OrderDate, 'yyyy-MM')
)

SELECT 
    SaleMonth,
    TotalSales,
    LAG(TotalSales, 1) OVER (ORDER BY SaleMonth) AS PreviousMonthSales,
    ROUND(
        (CAST(TotalSales AS FLOAT) - LAG(TotalSales) OVER (ORDER BY SaleMonth)) 
        / NULLIF(LAG(TotalSales) OVER (ORDER BY SaleMonth), 0) * 100, 2
    ) AS GrowthRatePercent
FROM MonthlySales
ORDER BY SaleMonth;
```

**Data Cleaning**
- Verified data types and ensured consistency in the SaleMonth format.

- One missing value in PreviousMonthSales and GrowthRatePercent was expected (first month has no prior data).

- No missing values in TotalSales.

**Outlier Detection**
- No outliers found in TotalSales or PreviousMonthSales.

- Five outliers identified in the GrowthRatePercent column with unusually high growth rates (e.g., 814%, 441%, etc.).

Examples of growth outliers:
- July 2011: +345.90%
- October 2011: +814.38%
- March 2014: +441.14%
  
These values were retained because they likely represent significant seasonal effects or business events, such as promotions or new product launches.

**Summary and Next Steps**

Monthly sales showed notable fluctuations with occasional spikes in growth.

The presence of outliers highlights potential peak-performance months worth deeper business investigation.

The cleaned and enriched dataset is now ready for Power BI visualization to uncover trends, seasonality, and actionable insights.



## Best-Selling Product Rankings by Country
---

**Business Questions**
- Are there any unusually high sales quantities in the dataset?

- Which products and countries do these high sales values belong to?

- Should these outliers be considered normal or treated in the analysis?

****Data Source and Extraction****

The data was extracted from the AdventureWorks database to find the top 5 best-selling products in each country.

We joined order, product, and location tables to:

Calculate total quantity sold per product in each country.

Rank products using DENSE_RANK() by quantity sold.

Filter to keep only the top 5 products per country.


```sql
WITH ProductSales AS (
    SELECT 
        cr.Name AS Country,
        p.Name AS ProductName,
        SUM(sod.OrderQty) AS TotalQuantity
    FROM Sales.SalesOrderHeader AS soh
    JOIN Sales.SalesOrderDetail AS sod ON soh.SalesOrderID = sod.SalesOrderID
    JOIN Production.Product AS p ON sod.ProductID = p.ProductID
    LEFT JOIN Person.Address AS addr ON soh.BillToAddressID = addr.AddressID
    LEFT JOIN Person.StateProvince AS sp ON addr.StateProvinceID = sp.StateProvinceID
    LEFT JOIN Person.CountryRegion AS cr ON sp.CountryRegionCode = cr.CountryRegionCode
    GROUP BY cr.Name, p.Name
),
RankedProducts AS (
    SELECT 
        Country,
        ProductName,
        TotalQuantity,
        DENSE_RANK() OVER (PARTITION BY Country ORDER BY TotalQuantity DESC) AS ProductRank
    FROM ProductSales
)
SELECT *
FROM RankedProducts
WHERE ProductRank <= 5
ORDER BY Country, ProductRank;
```


**Outlier Detection**

- No outliers detected in the ProductRank column.

- Five outliers detected in the TotalQuantity column, all related to products sold in the United States with exceptionally high sales volumes (over 3000 units).

- These outliers correspond to the top 5 ranked products, highlighting their strong sales performance in the U.S. market.

**Interpretation**
These high sales volumes likely reflect genuine market trends such as:

- Popular product demand

- Larger market size in the U.S.

- Possible promotional campaigns or seasonal effects

- Therefore, these outliers should not be removed and instead can provide valuable insights into market dynamics.

**Summary and Next Steps**

The dataset is clean and reliable, with clear outliers in sales quantity that represent real business phenomena.

Further analysis can explore factors driving these high sales and support strategic decision-making.

The data is ready for advanced visualization and reporting in Power BI to uncover deeper patterns by country and product.












