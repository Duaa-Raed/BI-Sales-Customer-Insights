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
