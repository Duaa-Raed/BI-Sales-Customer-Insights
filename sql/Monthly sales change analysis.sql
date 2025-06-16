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
