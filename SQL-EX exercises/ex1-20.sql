-- Exercise: 1
SELECT model, speed, hd 
FROM PC
WHERE price < 500

-- Exercise: 2
SELECT DISTINCT maker
FROM Product
WHERE type = 'Printer'

-- Exercise: 3
SELECT model, ram, screen
FROM Laptop
WHERE price > 1000

-- Exercise: 4
SELECT *
FROM Printer
WHERE color = 'y'

-- Exercise: 5
SELECT model, speed, hd
FROM PC
WHERE cd IN ('12x', '24x') AND price < 600

-- Exercise: 6
SELECT DISTINCT Product.maker, Laptop.speed
FROM Product, Laptop 
WHERE Product.model = Laptop.model AND Laptop.hd >= 10

-- Exercise: 7
SELECT DISTINCT PC.model, PC.price
FROM Product, PC
WHERE Product.model = PC.model AND Product.maker = 'B'
UNION
SELECT DISTINCT Laptop.model, Laptop.price
FROM Product, Laptop 
WHERE Product.model = Laptop.model AND Product.maker = 'B'
UNION
SELECT DISTINCT Printer.model, Printer.price
FROM Product, Printer
WHERE Product.model = Printer.model AND Product.maker = 'B'

-- Exercise: 8
SELECT DISTINCT maker
FROM Product
WHERE type IN ('PC')
EXCEPT
SELECT DISTINCT maker
FROM Product
WHERE type IN ('Laptop')

-- Exercise: 9
SELECT DISTINCT Product.maker
FROM Product, PC
WHERE Product.model = PC.model AND PC.speed >= 450

-- Exercise: 10
SELECT model, price 
FROM Printer 
WHERE price = (
	SELECT MAX(price) 
	FROM Printer)

-- Exercise: 11
SELECT AVG(PC.speed) AS Avg_speed
FROM PC

-- Exercise: 12
SELECT AVG(Laptop.speed) AS Avg_speed
FROM Laptop
WHERE Laptop.price > 1000

-- Exercise: 13
SELECT AVG(PC.speed) AS Avg_speed
FROM PC
JOIN Product
ON PC.model = Product.model
WHERE Product.maker = 'A'

-- Exercise: 14
SELECT Ships.class, Ships.name, Classes.country
FROM Ships
JOIN Classes ON Ships.class = Classes.class
WHERE numGuns >= 10

-- Exercise: 15
SELECT hd
FROM PC
GROUP BY hd
HAVING COUNT(hd) >= 2

-- Exercise: 16
SELECT DISTINCT A.model AS model_1, B.model AS model_2, A.speed, A.ram
FROM PC AS A, PC B
WHERE A.speed = B.speed AND A.ram = B.ram AND A.model > B.model

-- Exercise: 17
SELECT DISTINCT Product.type, Product.model, Laptop.speed
FROM Laptop
JOIN Product ON Laptop.model = Product.model
WHERE Laptop.speed<(
	SELECT MIN(PC.speed)
	FROM PC)

-- Exercise: 18
SELECT DISTINCT Product.maker, Printer.price
FROM Printer
JOIN Product
ON Printer.model = Product.model
WHERE Printer.color = 'y' AND Printer.price = (
	SELECT MIN(Printer.price)
	FROM Printer
	WHERE Printer.color = 'y')

-- Exercise: 19
SELECT DISTINCT Product.maker, AVG(Laptop.screen) AS Avg_screen
FROM Laptop
JOIN Product
ON Laptop.model = Product.model
GROUP BY maker

-- Exercise: 20
SELECT Product.maker, COUNT(Product.model) as Count_Model
FROM Product
WHERE type = 'pc'
GROUP BY maker
HAVING COUNT(Product.model) >= 3

-- Exercise: 21
SELECT Product.maker, MAX(PC.price)
FROM Product, PC
WHERE Product.model = PC.model
GROUP BY maker

-- Exercise: 22
SELECT speed, AVG(price) AS Avg_price
FROM PC
WHERE PC.speed > 600
GROUP BY speed