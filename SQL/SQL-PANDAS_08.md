# SQL/PANDAS_08

# 오늘은 복습을 하는 날!

`AVG()`, `GROUP BY`, `HAVING`, `DISTINCT` 등 지난 SQL 개념들을 복습합니다. 판다스에서 LEFT JOIN 하는 법`left.merge(right, on='id', how='left')`을 과제를 통해 복습합니다. 

8월 수업 중 [[Basic Statistics for Data Analysis](https://github.com/dataitgirls3/Teaching-Materials/blob/master/Basic%20Statistics%20for%20Data%20Analysis.ipynb)] 에서 나왔던 문제 풀이를 드디어 합니다. 부채를 갚는 기분이네요. 간단한 통계 함수를 파이썬으로 직접 구현하는 방법을 배우게 될 겁니다. → 종종 면접 문제로 나옴 

# SQL EVERYDAY 문제풀이

*Sharpen your SQL skills*

    ```SQL 
    -- 모드에서는 왜 from을 좀 띄어서 쓸 까? 
    SELECT year,
           month,
           COUNT(*) AS count
      FROM tutorial.aapl_historical_stock_price 
    			 -- #from하고 select를 맞추기 위해! (코드 가독성)
     GROUP BY year, month
     ORDER BY month, year
    
    ```
    

`AVG()`

- [https://mode.com/resources/sql-tutorial/sql-avg](https://mode.com/resources/sql-tutorial/sql-avg)

    아래 내용을 고민해보세요.

    > `AVG()` function ignores nulls completely. There are some cases in which you'll want to treat null values as 0. For these cases, you'll want to write a statement that changes the nulls to 0.

    - 솔루션

            ```SQL
            SELECT AVG(volume) AS avg_volume
            FROM tutorial.aapl_historical_stock_price
            
            
            -- null값이 있는 지 보는 방법 
            SELECT COUNT(*) - COUNT(volume)
            from tutorial.aapl_historical_stock_price
            ```

`GROUP BY`

- [https://mode.com/resources/sql-tutorial/sql-group-by](https://mode.com/resources/sql-tutorial/sql-group-by)

    아래 내용을 고민해보세요.

    > `GROUP BY` with column numbers generally recommended only when you're grouping many columns, or if something else is causing the text in the GROUP BY clause to be excessively long.

    - 솔루션

            ```SQL
            -- year을 넣어야지 month 뭉쳐서 안나옴 
            SELECT year,
                   month,
                   MIN(low) AS lowest_price,
                   MAX(high) AS highest_price
            FROM tutorial.aapl_historical_stock_price
            GROUP BY 1, 2  # group by를 컬럼 넘버로도 할 수 있음 
            ORDER BY 1, 2
            ```

`HAVING`

- [https://mode.com/resources/sql-tutorial/sql-having](https://mode.com/resources/sql-tutorial/sql-having)

    ```SQL
    
    SELECT year,
           month,
           MAX(high) AS month_high
    FROM tutorial.aapl_historical_stock_price
    GROUP BY 1, 2  
    HAVING MAX(high) > 400
    ;
    
    -- sub query로 만들기 
    SELECT year,
           month,
           high
    FROM tutorial.aapl_historical_stock_price
    GROUP BY 1, 2  
    HAVING (SELECT MAX(high)
    				FROM tutorial.aapl_historical_stock_price
    				WHERE MAX(high) > 400
    				)
    
    -- 애초에 400 밑인 애들을 날려버림 
    SELECT year, month, max(high)
    from (select *
          from tutorial.aapl_historical_stock_price
          where high > 400
          )
    group by year, month
    order by year, month
    
    
    -- 
    
    SELECT year, month, month_high
    FROM (
         select year, month, max(high) as month_high
         from tutorial.aapl_historical_stock_price
         group by year, month) df 
    where month_high > 400
    
    
    
    
    -- havign 절에 sub query 넣을 상황 
    -- 다른 주식하고 비교할 때 
    SELECT year,
           month,
           MAX(high) AS month_high
    FROM tutorial.aapl_historical_stock_price
    GROUP BY 1, 2  
    HAVING  MAX(high) > (select max(high) from tutorial.historical_samsung_stock_price) 
    
    
    -- WHERE절에 aggre 연산 쓰지 말기 
    ```
    
    

`DISTINCT`

- [https://mode.com/sql-tutorial/sql-distinct](https://mode.com/sql-tutorial/sql-distinct)

    아래 내용을 고민해보세요.

    > You'll notice that `DISTINCT` goes inside the aggregate function rather than at the beginning of the `SELECT` clause. Of course, you can `SUM` or `AVG` the distinct values in a column, but there are fewer practical applications for them.

    ```sql
    -- agg 함수는 만들고 as 주면 좋음 
    -- distinct를 aggre 함수 안에 쓸 수 있음 
    SELECT COUNT(DISTINCT month) AS unique_months
    FROM tutorial.aapl_historical_stock_price
    
    -- 잘못된 예시 
    SELECT DISTINCT COUNT(month) -- aggre 함수 밖에 distinct 쓰지 말기 
    FROM tutorial.aapl_historical_stock_price
    
    ```

    -- 선미님의 코드 
    ```sql
    /* Write a query that calculates 
    the average daily trade volume for Apple stock.*/
    SELECT AVG(volume)
    FROM tutorial.aapl_historical_stock_price;
    /* Calculate 
    the total number of shares traded each month. 
    Order your results chronologically. */
    SELECT year
         , month
         , SUM(volume)
    FROM tutorial.aapl_historical_stock_price
    GROUP BY year, month
    ORDER BY year, month;
    /* Write a query 
    that calculates the lowest and highest prices 
    that Apple stock achieved each month. */
    SELECT year
        , month
        , MIN(low)
        , MAX(high)
    FROM tutorial.aapl_historical_stock_price
    GROUP BY year, month
    ORDER BY year, month;
    /* HAVING to subquery */
    SELECT year,
           month,
           MAX(high) AS month_high
      FROM tutorial.aapl_historical_stock_price
     GROUP BY year, month
    HAVING MAX(high) > 400
    ;
    SELECT year
         , month
         , month_high
    FROM (
          SELECT year,
                 month,
                 MAX(high) AS month_high
          FROM tutorial.aapl_historical_stock_price
          GROUP BY year, month
    ) df
    WHERE month_high > 400
    ;
    SELECT year, month, MAX(high)
    FROM tutorial.aapl_historical_stock_price
    WHERE high > 400
    GROUP BY year, month
    ORDER BY year, month
    ;
    /* DISTINCT */
    SELECT COUNT(DISTINCT year)
    FROM tutorial.aapl_historical_stock_price
    ;
    /* Write a query 
    that separately counts the number of unique values in the month column 
    and the number of unique values in the `year` column. */
    SELECT COUNT(DISTINCT year) count_year
         , COUNT(DISTINCT month) count_month
    FROM tutorial.aapl_historical_stock_price
    ```

# Pandas `merge`, `apply`

- Pandas LEFT JOIN 과제 풀이
- Pandas `apply()`와 Python `lambda` 함수
- 8월 수업 중 [[Basic Statistics for Data Analysis](https://github.com/dataitgirls3/Teaching-Materials/blob/master/Basic%20Statistics%20for%20Data%20Analysis.ipynb)] 문제 풀이 (간단한 통계 계산하는 함수 직접 구현하기)

# 9월 26일 목요일 수업

- SQL EVERYDAY 과제 풀이
- Pandas `apply()`와 Python `lambda` 함수 과제 풀이
- [Python Comprehension](https://github.com/dataitgirls3/Teaching-Materials/blob/master/Comprehension.ipynb)

# 판다스 run 처음부터 끝까지 다시 할 수 있는 방법

- cell - run all / run above(내 셀 위의꺼까지 싹 run)