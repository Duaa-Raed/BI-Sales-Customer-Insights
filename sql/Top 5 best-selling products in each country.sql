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
