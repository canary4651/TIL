# SQL 03

```sql
-- LIMIT : 맨 위에 있는 거 한줄만 
    SELECT * 
    FROM Customers
    LIMIT 1
    ;
    
    -- ORDER BY :정렬 / 오름차순: 작은 값부터 큰 값으로 (asc) 
    SELECT *
    FROM Customers
    ORDER BY CustomerID ASC
    ;
    
    ---- 작은순서대로 정렬 (디폴트값이 asc)
    SELECT *
    FROM customers
    WHERE ----- 
    ORDER BY customerid; 
    
    ----정렬이 이상한 표에서 작은 순서대로 하고 1줄만 구하라고 할 때 위에를 응용해서 하면 됨 
    
    
    SELECT *
    FROM Customers
    ORDER BY CustomerID DESC --내림차순: 큰값부터 작은 값 쪽으로의 순서
    ;
    
    -- ORDER BY and LIMIT
    SELECT *
    FROM Customers
    ORDER BY CustomerID DESC
    LIMIT 1
    ;
    

    --HACKER RANK : Higher Than 75 Marks
    SELECT NAME
    FROM STUDENTS
    WHERE MARKS > 75
    ORDER BY RIGHT(name,3), ID ASC;
    
    /*
    Employee Names
    Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
    */
    SELECT NAME
    FROM EMPLOYEE
    ORDER BY name
    
    --- 기본적으로 order by 하면 알파벳으로 정렬이 된다 
    
    --Employee Salaries
    /*
    Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than 2000 per month who have been employees for less than 10  months. Sort your result by ascending employee_id.
    */
    SELECT NAME
    FROM employee
    WHERE salary>2000 and months<10
    ORDER BY employee_id
    
    --Weather Observation Station 15
    /*
    Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to 4 decimal places.
    */
    SELECT ROUND(LONG_W,4)
    FROM STATION
    WHERE LAT_N < 137.2345
    ORDER BY LAT_N DESC
    LIMIT 1
    ;
    
    --Weather Observation Station 17
    /*
    Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than . Round your answer to  decimal places.
    */
    SELECT ROUND(LONG_W,4)
    FROM STATION
    WHERE LAT_N > 38.7780
    ORDER BY LAT_N ASC
    LIMIT 1
    ;
```    
    

<BR>

# GROUP BY 데이터 요약

- 구글드라이브: [http://tiny.cc/gojqaz](http://tiny.cc/gojqaz)

```sql
    -- GROUP BY와 집계함수(AVG(), SUM(), MIN(), MAX(), COUNT())
        SELECT Company
             , AVG(Salary) as AVERAGE
             , SUM(Salary) as SUMMATION
        FROM www_salary
        GROUP BY Company
        /*
        Company  AVERAGE       SUMMATION
        바로     1771.428571   12400
        유니콘    4750          9500
        */
        
        /*
        주의사항
        집계함수안의 컬럼 이외의 컬럼들은 **SELECT,GROUP BY에 동시**에 기술해야 합니다.
        */
        
        -- ORDER BY와 GROUP BY
        SELECT Company, AVG(Salary)
        FROM www_salary
        GROUP BY Company
        ORDER BY AVG(Salary)
        
        -- HAVING
        SELECT Company
             , AVG(Salary) as AVERAGE
        FROM www_salary
        GROUP BY Company
        HAVING AVG(Salary) > 3000
        /*
        Company  AVERAGE
        유니콘    4750
        */
```
- 데이터를 요약한다고 생각하면 됨
- group by의 조건문은 having절 like where절! (limit절하고도 비슷)

<br>

- 연습문제

[https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

- 연습문제 1
OrderDetails 테이블을 사용해, Order별로 몇 개의 상품을 주문했는지 보여주세요.
```sql
        SELECT Orderid, sum(Quantity)
        FROM OrderDetails
        GROUP BY Orderid

    SELECT orderid
    		, count(productid)
    FROM orderdetails
    group by orderid;
```
- 연습문제 2
Products 테이블을 참조해, 공급하는 물건들의 평균 가격이 비싼 Supplier 다섯 업체와 평균 가격을 출력하세요.
```sql
        SELECT SupplierID, AVG(Price)
        FROM Products
        GROUP BY SupplierID
        ORDER BY AVG(Price) DESC
        LIMIT 5

    SELECT supplierid
    		, avg(price)
    FROM products
    GROUP BY supplierid
    ORDER BY AVG(price) desc
    limit 5
    ;
```
- 연습문제 3
Products 테이블을 참조해, 공급하는 물건들의 평균 가격이 40 이상인 업체와 평균 가격을 출력하세요.
```sql
        SELECT SupplierID, AVG(Price)
        FROM Products
        GROUP BY SupplierID
        ORDER BY AVG(Price) DESC
        HAVING AVG(Price) > 40

    SELECT supplierid
    		, avg(price)
    FROM products
    GROUP BY supplierid
    HAVING AVG(PRICE) >= 40
    ;
```
- ORDER by는 마지막 정렬이라고 생각하면 된다

<br>

# SQL JOIN

<br>

- [눈으로 보는 조인](https://sql-joins.leopard.in.ua/)
- [예제코드](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

<br>

앞으로는 Orders, 주문 테이블을 기준으로 여러 테이블을 엮어보는 연습을 하겠습니다. 먼저 Orders 테이블을 살펴볼까요.
```sql
    SELECT *
    FROM Orders
    LIMIT 4;
    
    /*
    OrderID	CustomerID	EmployeeID	OrderDate	  ShipperID
    10248	  90	        5	          1996-07-04	3
    10249	  81	        6	          1996-07-05	1
    10250  	34	        4	          1996-07-08	2
    10251	  84	        3	          1996-07-08	1
    */
```

주문 하나가 발생 할 때마다 한 줄씩 쌓이는 테이블처럼 보입니다. 

OrderID는 1개의 주문을 대표하는 번호일테고, CustomerID는 고객, EmployeeID는 판매사원, OrderDate는 판매가 된 날짜, ShipperID는 배송업체일 겁니다. OrderDate를 제외하고는 모두 ID만 남아있네요. 디테일을 보기 위해서는 다른 테이블을 참조해야 할 것 같습니다. 

저는 주문을 누가 했는지가 첫 번째로 궁금합니다. Customers 테이블에 그 정보가 있을 것 같습니다. 테이블에 정보가 많으니까 일련번호(CustomerId)와 고객 이름(CustomerName), 나라(Country)만 찍어보겠습니다.

```sql
    SELECT CustomerID, CustomerName, Country
    FROM Customers
    LIMIT 5;
    
    /*
    CustomerID	CustomerName	                       Country
    1	          Alfreds Futterkiste	                 Germany
    2	          Ana Trujillo Emparedados y helados	 Mexico
    3	          Antonio Moreno Taquería	             Mexico
    4	          Around the Horn	                     UK
    5	          Berglunds snabbköp	                 Sweden
    */
```
CustomerID가 1번인 사람의 이름은 Alfreds Futterkiste고, 독일에 사네요. 

<br>

그러면 1996년 7월 4일에 OrderID 10248를 만들며 주문을 한 CustomerID 90번 고객의 이름은 어떻게 알아낼 수 있을까요?
```sql
    SELECT CustomerID, CustomerName, Country
    FROM Customers
    WHERE CustomerID = 90
    
    /*
    CustomerID	CustomerName	Country
    90	        Wilman Kala	  Finland
    */
```
귀찮습니다. 매번 궁금한게 생길 때마다 이렇게 조회해보는 방법밖에 없을까요? SQL을 이용하면 여러 테이블들을 한 번에 묶어 볼 수 있습니다!
```sql
    SELECT *
    FROM ORDERS AS O 
    			INNER JOIN CUSTOMERS AS C ON O.CUSTOMERID = C.CUSTOMERID;
```
앞의 예시를 SQL로 좀 더 편하게 볼 수 있는 형태로 출력해 보겠습니다. 두 테이블은 CustomerID로 엮을 수 있겠죠?

- JOIN으로 큰 테이블을 만든다 라고 생각
```sql
## INNER JOIN

    SELECT *
    FROM Orders
         INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
    ;
    
    /*
    Alias(별명)을 사용해서 코드를 좀 더 간결하게 쓸 수 있습니다. 정렬도 해볼게요.
    */
    
    SELECT *
    FROM Orders AS o
         INNER JOIN Customers AS c ON o.CustomerID = c.CustomerID
    ORDER BY c.CustomerName;
    
    /*
    정보가 너무 많으니까, 보고싶은 것만 출력해보겠습니다.
    */
    
    SELECT o.OrderDate, c.CustomerID, c.CustomerName, c.Country
    FROM Orders AS o
         INNER JOIN Customers as c ON o.CustomerID = c.CustomerID
    ORDER BY c.CustomerName;
```
양 테이블에 모두 데이터가 있는 것만 보고 싶을 때 우리는 INNER JOIN을 사용합니다. LEFT JOIN을 보면 INNER JOIN을 더 잘 이해할 수 있습니다.

복습을 할 때는 접어놓고 풀어보세요 :)

- OrderID 10248번에는 몇 가지 종류의 상품이 들어있나요? 상품들의 총 갯수는 어떻게 되나요? Orders, OrderDetails 테이블을 이용해 알아보세요.
```sql
        SELECT OrderDetails.OrderID
             , OrderDetails.ProductID
             , OrderDetails.Quantity
        FROM Orders
             INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
        WHERE Orders.OrderID = 10248
        ;
        
        /*
        3가지 종류의 상품 (ProductID 11, 42, 72)
        총 27개 (Quantity 12+10+5)
        */
        
        /* 좀 더 세련된 방법 */
        SELECT Orders.OrderID
             , COUNT(OrderDetails.ProductID)
             , SUM(OrderDetails.Quantity)
        FROM Orders
             INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
        WHERE Orders.OrderID = 10248
        GROUP BY Orders.OrderID
        
        /* 세련된 방법2 똑같은 결과가 나오지만 WHERE 대신 HAVING을 활용 */
        SELECT Orders.OrderID
             , COUNT(OrderDetails.ProductID)
             , SUM(OrderDetails.Quantity)
        FROM Orders
             INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
        GROUP BY Orders.OrderID
        HAVING Orders.OrderID = 10248

    SELECT ORDERDETATILS.ORDERID
    			,COUNT(ORDERDETAILS.PRODUCTID)
    			,SUM(ORDERDETATILS.QUANTITY)
    FROM ORDERS
    	INNER JOIN ORDERDETATILS ON ORDERS.ORDERID = ORDERDETATILS.ORDERID
    WHERE ORDERS.ORDERID = 10248
    

    /*
    OrderID 10248번에는 몇 가지 종류의 상품이 들어있나요? 상품들의 총 갯수는 어떻게 되나요? Orders, OrderDetails 테이블을 이용해 알아보세요.
    */
    SELECT OrderDetails.OrderID
    	, OrderDetails.PRODUCTID
        , OrderDetails.Quantity
    FROM Orders 
    	INNER JOIN OrderDetails ON OrderDetails.OrderID = Orders.OrderID
    WHERE Orders.OrderID = 10248
    
```
- OrderID 10249번에는 어떤 상품들이 들어있나요? 상품명을 출력하세요.
```sql
        SELECT o.OrderID, o.OrderDate, od.Quantity, p.ProductName, p.Price
        FROM Orders AS o
             INNER JOIN OrderDetails AS od ON o.OrderID = od.OrderID
             INNER JOIN Products AS p ON od.ProductID = p.ProductID
        WHERE o.OrderID = 10249
        
        /*
        Tofu
        Manjumup Dried Apples
        */

    /*
    OrderID 10249번에는 어떤 상품들이 들어있나요? 상품명을 출력하세요
    */
    SELECT Products.Productname
    FROM Orders 
    	INNER JOIN Orderdetails on Orders.OrderID = Orderdetails.OrderID
    	INNER JOIN Products on Products.ProductID = Orderdetails.ProductID
    WHERE Orders.OrderID = 10249
```
- OrderID 10249번에 들어있는 상품들의 총 가격은 얼마인가요?
```sql
        SELECT o.OrderID, p.ProductName, od.Quantity, p.Price
        FROM Orders AS o
             INNER JOIN OrderDetails AS od ON o.OrderID = od.OrderID
             INNER JOIN Products AS p ON od.ProductID = p.ProductID
        WHERE o.OrderID = 10249
        
        /*
        OrderID	 ProductName	          Quantity	Price
        10249	   Tofu	                  9	        23.25
        10249	   Manjimup Dried Apples	40	      53
        */
        
        /*
        2329.25
        */
        
        /* 좀 더 세련된 방법 */
        SELECT o.OrderID
             , SUM(od.Quantity * p.Price)
        FROM Orders AS o
             INNER JOIN OrderDetails AS od ON o.OrderID = od.OrderID
             INNER JOIN Products AS p ON od.ProductID = p.ProductID
        WHERE o.OrderID = 10249
        GROUP BY o.OrderID
        
        /* 좀 더 세련된 방법2 */
        SELECT o.OrderID
             , SUM(od.Quantity * p.Price) as order_price
        FROM Orders AS o
             INNER JOIN OrderDetails AS od ON o.OrderID = od.OrderID
             INNER JOIN Products AS p ON od.ProductID = p.ProductID
        GROUP BY o.OrderID
        HAVING o.OrderID = 10249

    SELECT orders.orderid, products.productid, orderdetails.quantity, products.price
    	, sum(orderdetails.quantity *products.price)
    FROM ORDERS
    	INNER JOIN Orderdetails on orders.orderid = orderdetails.orderid
    	INNER JOIN Products on Orderdetails.productid = products.productid
    where orders.orderid = 10249
```
- OrderID 10249번에 들어있는 상품명, 납품한 업체 이름, 업체가 소속된 국가를 모두 출력하세요.
```sql
        SELECT o.OrderID, o.OrderDate, p.ProductName, s.SupplierName
        FROM Orders AS o
             INNER JOIN OrderDetails AS od ON o.OrderID = od.OrderID
             INNER JOIN Products AS p ON od.ProductID = p.ProductID
             INNER JOIN Suppliers AS s ON p.SupplierID = s.SupplierID
        WHERE o.OrderID = 10249
        
        /*
        OrderID	ProductName	           SupplierName	  Country
        10249	  Tofu	                 Mayumi's	      Japan
        10249	  Manjimup Dried Apples	 G'day, Mate	  Australia
        */

    SELECT Products.productname, suppliers.suppliername, suppliers.country
    FROM orders
    	INNER JOIN Orderdetails on orders.orderid = orderdetails.orderid
    	INNER JOIN Products on Orderdetails.productid = products.productid
    	INNER JOIN suppliers on products.supplierid = suppliers.supplierid
    WHERE ORDERS.ORDERID = 10249
```
이번에는 Customers 테이블을 기준으로 생각 해봅시다. 가입을 해서 고객 정보는 있는데, 주문을 한 번도 하지 않은 고객이 있는지 궁금합니다. 첫 구매를 유도하기 위해서 이런 고객을 대상으로 다양한 프로모션을 시도 해 볼 수 있겠지요? 이럴 때 LEFT JOIN을 사용할 수 있습니다.
```sql
## LEFT JOIN

    SELECT c.CustomerID AS c_customerID
         , o.CustomerID AS o_customerID
         , c.CustomerName
         , o.*
    FROM Customers 
         LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    LIMIT 5
    ; 
    
    /*
    c_customerID	o_customerID	CustomerName	                      OrderID	CustomerID	EmployeeID	OrderDate	  ShipperID
    1	            null	        Alfreds Futterkiste	                null	  null	      null	      null	      null
    2	            2	            Ana Trujillo Emparedados y helados	10308	  2	          7	          1996-09-18	3
    3	            3	            Antonio Moreno Taquería	            10365	  3	          3	          1996-11-27	2
    4	            4	            Around the Horn	                    10355	  4	          6	          1996-11-15	1
    4	            4	            Around the Horn	                    10383	  4	          8	          1996-12-16	3
    */
```
Customers 테이블에는 데이터가 있는 ID 1번 고객은 Orders 테이블에는 데이터가 없습니다. 확인 해볼까요?
```sql
    SELECT *
    FROM Orders
    WHERE CustomerID = 1
    
    /*
    No result.
    */
```
복습을 할 때는 답을 접은채로 풀어보세요 :) 

- 그렇다면, 가입은 했지만 한 번도 주문을 하지 않은 고객이 또 있는지 어떻게 확인 할 수 있을까요?
```sql
        SELECT c.CustomerID AS c_customerID
             , c.CustomerName
             , o.*
        FROM Customers AS c
             LEFT JOIN Orders as o ON c.CustomerID = o.CustomerID
        WHERE o.CustomerID IS NULL

    SELECT customers.customerid 
    	, ORDERS.customerid 
    	, customers.customername
    	, orders.*
    from customers
    	LEFT JOIN ORDERS ON ORDERS.CUSTOMERID = CUSTOMERS.customerid
    WHERE ORDERS.CUSTOMERID IS NULL
    ;
```
- 가입은 했지만, 한 번도 주문을 하지 않은 고객은 총 몇 명인가요?
```sql
        SELECT COUNT(c.CustomerID) AS no_order
        FROM Customers AS c
             LEFT JOIN Orders as o ON c.CustomerID = o.CustomerID
        WHERE o.CustomerID IS NULL

    SELECT COUNT(CUSTOMERS.CUSTOMERID)
    FROM CUSTOMERS
    	LEFT JOIN ORDERS ON ORDERS.CUSTOMERID = CUSTOMERS.customerid
    WHERE ORDERS.CUSTOMERID IS NULL
    ;
```
- 주문을 한 번도 성사시키지 못 한 직원이 있나요?
```sql
        SELECT e.FirstName, e.LastName, e.Notes
        FROM Employees AS e
             LEFT JOIN Orders AS o ON o.EmployeeID = e.EmployeeID
        WHERE o.OrderID IS NULL
        
        /*
        FirstName	LastName	Notes
        Adam	    West	    An old chum.
        */
        
        /* 
        Adam West는 사장의 오랜 친구랍니다. 
        물건을 하나도 팔지 못했지만 여전히 회사를 다닐 수 있는 비결일까요! 
        */

    SELECT e.LastName, E.firstname , E.notes
    FROM employees as e
    	LEFT JOIN ORDERS ON E.employeeid = orders.employeeid
    where Orders.OrderID is null
```
LeetCode 연습문제:

- [175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)
```sql
    # 왜 안나오는 지 궁금... 오타였음 ^^ 
    SELECT firstname, lastname, city, state
    FROM person
        LEFT JOIN address on person.personid = address.personid 
    ;
```
- [181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)
```sql
    SELECT e1.name as Employee
    FROM employee as e1, employee as e2
    WHERE e1.managerid = e2.id 
        and e1.salary > e2.salary;
```
- [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)
```sql
    SELECT DISTINCT Email
    FROM PERSON AS P
    GROUP BY Email
    HAVING count(email) > 1
```
- [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/)
```sql
    SELECT c.name as customers 
    FROM customers as c
        LEFT JOIN orders as o on c.id =  o.customerid
    WHERE o.customerid is null
    ;
```
- [196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/)
```sql
    # 이 문제 이해가 안감.... 
    
    SELECT *
    FROM PERSON as p1, person as p2
    WHERE P1.email = p2.email
        and p1.id < p2.id
    ;
    
    # 이게 맞는 거 아닌가..? 어렵다 낼 물어보자 

    DELETE P1.*
    FROM PERSON as P1, PERSON as P2
    WHERE P1.EMAIL = P2.EMAIL 
        AND P1.ID > P2.ID
    ;
```