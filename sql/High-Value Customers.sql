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
