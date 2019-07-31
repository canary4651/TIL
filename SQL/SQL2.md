# sql 기초 1
select → 컬롬
from → 테이블
whhere → row에 대한 이야기

count 개수 max min distinct 

* 스몰데이터 : 내가 데이터를 만들어서 분석해보고 해석해보는 경험 ex) 강의 피드백, 기분점수, 슬랙_이모티콘

* 크롤링 → 데이터를 끌어오는 것 / 그치만 이미 회사에 가면 데이터가 쌓여있기 때문에 sql 먼저 깊이 배움 

* 일정 수준의 지식이 쌓이는 게 sql 

* 너무 걱정할 필요 없음

sum 합계
min/max
avg (평균)
round(avg) -> 비슷한 평균값
해커랭크 풀이하기

SQL statement: 
-- as: 여러개의 테이블이 있을 때 겹칠 수도 있기 때문에 지정 (별칭) 알리아스) / 행에도 줄 수 있음 
```sql
select *
from customers AS c
```
```sql
select rounc(avg(lat_n)) as lat
from customers as c 
```
-- between and 
```sql
select name, salary 
from employess
where salary betwwen 5000 and 6000
```

-> 연봉이 오천과 육천 사이의 모든 사람 
```SQL
SELECT 
FROM
WHERE 5000 < SALARY
AND SALARY =< 6000
```


-- IN
```SQL
SELECT NAME, SALARY
FROM EMPLOYYES 
WHERE SALARY IN (5000, 6000)
``` 
-> 5000, 6000 인 사람만 출력 

-- WHERE DISTRICT = 'CALIFORNIA' -> 대소문자 구별 꼭! 



## Revising Aggregations - The Count Function
* Query a count of the number of cities in CITY having a Population larger than 100000.
```sql
SELECT COUNT(ID)
FROM CITY
WHERE POPULATION > 100000
```

## Revising Aggregations - The Sum Function
* Query the total population of all cities in CITY where District is California.

```sql
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'CALIFORNIA'
```

## Revising Aggregations - Averages
* Query the average population of all cities in CITY where District is California.

```sql
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'CALIFORNIA'
```

## Average Population
* Query the average population for all cities in CITY, rounded down to the nearest integer.

```sql
SELECT ROUND(AVG(POPULATION))
FROM CITY
```

## Japan Population
* Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.

```SQL
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = 'JPN'
```



## Population Density Difference
* Query the difference between the maximum and minimum populations in CITY.

```SQL
SELECT MAX(POPULATION)
- MIN(POPULATION)
FROM CITY)
```


## Aggregation > Weather Observation Station 2
* Query the following two values from the STATION table:

        The sum of all values in LAT_N rounded to a scale of  decimal places 2. 
        The sum of all values in LONG_W rounded to a scale of  decimal places2 .

```SQL
SELECT ROUND(SUM(LAT_N),2)
, ROUND(SUM(LONG_W,2))
FROM CITY;
```
* 이 문제 자꾸 틀림;;;


## Weather Observation Station 13
* Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7780 and less than 137.2345. Truncate your answer to  decimal places 4.

```SQL
SELECT ROUND(SUM(LAT_N),4)
FROM STATION
WHERE LAT_N > 38.7780
AND LAT_N < 137.2345
```

## Weather Observation Station 14
* Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to  decimal places 4.

```SQL
SELECT ROUNC(MAX(LAT_N),4)
FROM STATION
WHERE LAT_N < 137.2345
````

## Weather Observation Station 16
* Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780. Round your answer to  decimal places.

````SQL
SELECT ROUNC(MIN(LAT_N),4)
FROM STATION
WHERE LAT_N > 38.7780
```

# 스몰데이터

* 첫번째 팀별 활동 
- 7월 25일 목요일 스몰데이터 (1) 아이디어 정립과 데이터 수집 방법에 대한 회의. 데이터 수집 시작.
- 8월 9일 금요일 스몰데이터 (2) 수집하고 있는 데이터에 대한 발표. 시행착오 공유. 간단한 분석.
- 8월 23일 금요일 스몰데이터 (3) 지난 한 달간 수집한 데이터에 대한 발표와 분석 결과 공유. 발전방향 논의.
    * 2조_데이터분석아이디어 https://www.notion.so/canary4651/2-_-2215306da791454cabf3a5db643eae11