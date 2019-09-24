# SQL 07

# MOOD 문제 풀이

*Sharpen your SQL skills*

`COUNT(*)`와 `COUNT(지정컬럼)`의 차이점에 대해서 

- [https://mode.com/resources/sql-tutorial/sql-count](https://mode.com/resources/sql-tutorial/sql-count)
```sql
    # 선미님의 실수 
    select sum(high)/count(*) -> 요런 실수
    from table
    
    # * 해버리면 모든 칸들을 다 값으로 세버리니까 (null)값이 들어감 
    
    select sum(high)/count(high) -> 이렇게 고쳐야함
    from table
    
    
    #avg 함수를 쓰면 안 될 때? 
    
    select sum(high)/count(high) #high에 있는 null 값을 0으로 쳐서 더하고/ count해줌(포함해줌)
    from table
    
    
    select avg(high) 
    from table
    
    # 다를 때도 있음 
    # 노트필기 참고 
```
`SUM()`

- [https://mode.com/resources/sql-tutorial/sql-sum](https://mode.com/resources/sql-tutorial/sql-sum)
- 평균을 구해라?
    - avg()를 쓰지 않고 sum()/count() 이렇게 구해야 할 때도 있음
```sql
    SELECT SUM(p.open) / COUNT(p.open)
    FROM tutorial.aapl_historical_stock_price p
    
    /* 아래 솔루션은 어떤가요? */
    SELECT SUM(p.open) / COUNT(*)
    FROM tutorial.aapl_historical_stock_price p;
    
    SELECT SUM(p.open) / COUNT(1)
    FROM tutorial.aapl_historical_stock_price p;
```
## 9월 24일 과제

`AVG()`

- [https://mode.com/resources/sql-tutorial/sql-avg](https://mode.com/resources/sql-tutorial/sql-avg)

    아래 내용을 고민해보세요.

    > `AVG()` function ignores nulls completely. There are some cases in which you'll want to treat null values as 0. For these cases, you'll want to write a statement that changes the nulls to 0.

`GROUP BY`

- [https://mode.com/resources/sql-tutorial/sql-group-by](https://mode.com/resources/sql-tutorial/sql-group-by)

    아래 내용을 고민해보세요.

    > `GROUP BY` with column numbers generally recommended only when you're grouping many columns, or if something else is causing the text in the GROUP BY clause to be excessively long.

- group by  쓸 때 select 절에도 컬럼 이름을 해주어야 하는 데, group by 1, 2 이렇게 쓰는 기능도 있긴 있음. 하지만 10개정도 될 때 쓰자...!

`HAVING`

- [https://mode.com/resources/sql-tutorial/sql-having](https://mode.com/resources/sql-tutorial/sql-having)

`DISTINCT`

- [https://mode.com/sql-tutorial/sql-distinct](https://mode.com/sql-tutorial/sql-distinct)

    아래 내용을 고민해보세요.

    > You'll notice that `DISTINCT` goes inside the aggregate function rather than at the beginning of the `SELECT` clause. Of course, you can `SUM` or `AVG` the distinct values in a column, but there are fewer practical applications for them.

## 9월 26일 목요일 과제

[프로그래머스 코딩테스트 고득점 Kit](https://programmers.co.kr/learn/challenges?tab=practice_kit), 6개 문제

`SELECT`

- 동물의 아이디와 이름 / 여러 기준으로 정렬하기
- 상위 n개 레코드 (`ORDER BY`, `LIMIT` 풀이 이외에, `WHERE` 절 서브쿼리를 사용해서 풀어보세요)

`SUM`, `MAX`, `MIN`

- 최댓값 구하기 (`ORDER BY`, `LIMIT` 풀이 이외에, `WHERE` 절 서브쿼리를 사용해서 풀어보세요)
- 동물 수 구하기 / 중복 제거하기

# Pandas `merge`, `apply`

- Pandas LEFT JOIN 과제 풀이
- Pandas `apply()`와 Python `lambda` 함수
- 8월 수업 중 [[Basic Statistics for Data Analysis](https://github.com/dataitgirls3/Teaching-Materials/blob/master/Basic%20Statistics%20for%20Data%20Analysis.ipynb)] 문제 풀이 (간단한 통계계산하는 함수 직접 구현하기)

# 9월 26일 목요일 수업

- SQL EVERYDAY 과제 풀이
- Pandas 과제풀이
- [Python Comprehension](https://github.com/dataitgirls3/Teaching-Materials/blob/master/Comprehension.ipynb)

# challenges