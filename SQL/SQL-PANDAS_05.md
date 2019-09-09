# SQL/PANDAS_05

# 서브쿼리

- 서브쿼리 추가설명
[184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/)
[Contest Leaderboard](https://www.hackerrank.com/challenges/contest-leaderboard/problem?h_r=next-challenge&h_v=zen)

    /* 서브쿼리: 쿼리 결과를 또 하나의 테이블 처럼 사용 할 수 있음 */
        /* 베이스라인 */
        SELECT *
        FROM (
             SELECT d.name -- 부서 이름 (IT, Sales 등)
                  , d.id -- 부서 id
                  , max(e.salary) AS department_max_salary -- 부서 최고 연봉
             FROM employee AS e
                  INNER JOIN department AS d ON e.departmentid = d.id
             GROUP BY d.name, d.id -- 부서 별 최고 연봉을 찾기 위해 그룹화
             ) AS df

- where 절에서 서브쿼리

    -- 서브쿼리에서 반환하는 값이 1개일 때 (스칼라, 값)
    SELECT i.ANIMAL_ID, i.NAME
    FROM ANIMAL_INS i
    WHERE i.DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS)
    
    -- 서브쿼리에서 반환하는 값이 2개 이상일 때 (벡터, 리스트)
    SELECT i.ANIMAL_ID, i.NAME
    FROM ANIMAL_INS i
    WHERE i.DATETIME IN (
        SELECT MIN(DATETIME)
        FROM ANIMAL_INS
        UNION
        SELECT MAX(DATETIME)
        FROM ANIMAL_INS
    )

# [sql 7일 챌린지](https://programmers.co.kr/events/7day-sql?utm_source=programmers&utm_medium=learn_7daySQL&utm_campaign=7daySQL)

- 문자열을 다루는 함수들 (LEFT(), RIGHT(), SUBSTRING_INDEX())
[보호소에서 중성화한 동물](https://programmers.co.kr/learn/courses/30/lessons/59045)
- left(함수) →left(컬럼 문자열, 숫자 정수) / right(함수)
    - left('apple',3) → app
    - right('apple',3) → ple
- substring_index(컬럼, '공백',1) : 공백을 기준으로 1번째를 잘라서 섭스트링으로 가지고 와라
    - substring_index('hello world','',1) → hello

    SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
    FROM ANIMAL_INS i
         INNER JOIN ANIMAL_OUTS ot ON i.ANIMAL_ID = ot.ANIMAL_ID
    WHERE SUBSTRING_INDEX(i.SEX_UPON_INTAKE, ' ', 1) = 'Intact'
    AND SUBSTRING_INDEX(ot.SEX_UPON_OUTCOME, ' ', 1) IN ('Spayed', 'Neutered')
    
    # 혹은
    SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
    FROM ANIMAL_INS i
         INNER JOIN ANIMAL_OUTS ot ON i.ANIMAL_ID = ot.ANIMAL_ID
    WHERE LEFT(i.SEX_UPON_INTAKE,6) = 'INTACT'
    OR (
    LEFT(OT.SEX_UPON_OUTCOME,8) IN ('SPATED', 'NEUTERED'))
    
    # 근데 left 함수 쓰려면 순서를 다 세야하니까 귀찮으니까 substring index 함수로 위로 풀어줌. 
    
    
    
    # 단비님 풀이 
    SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
    FROM ANIMAL_INS AS I INNER JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID
    WHERE I.SEX_UPON_INTAKE <> O.SEX_UPON_OUTCOME
    ORDER BY I.ANIMAL_ID
    
    
    #내 풀이
    SELECT AO.ANIMAL_ID, AO.ANIMAL_TYPE, AO.NAME
    FROM
        (
        SELECT *
        FROM ANIMAL_INS A
        WHERE SEX_UPON_INTAKE LIKE "Intact%"
        ) A1, ANIMAL_OUTS AO
    WHERE A1.ANIMAL_ID = AO.ANIMAL_ID
    AND AO.SEX_UPON_OUTCOME NOT LIKE "Intact%"
    
    # 내 풀이 2번째
    SELECT AI.ANIMAL_ID, AI.ANIMAL_TYPE, AI.NAME
    FROM ANIMAL_INS AS AI 
        left join ANIMAL_OUTS AS AO on ai.animal_id = ao.animal_id
    WHERE AI.SEX_UPON_INTAKE like 'Intact%' 
        and AO.SEX_UPON_OUTCOME NOT like 'Intact%'
    ORDER BY AI.ANIMAL_ID;

- LIKE '%{something}%', UPPER(), LOWER()
[이름에 el이 들어가는 동물 찾기](https://programmers.co.kr/learn/courses/30/lessons/59047)
- upper(다 대문자로 바꿔주는 함수)
- lower(다 소문자로 바꿔주는 함수)
- upper 사용 왜냐면! el, EL, eL, El 일 수도 있으니까 4가지 커버를 다 해줄 함
- 그래서 [i.name](http://i.name) 칼럼을 다 대문자로 바꿔주고 시작!
- 대문자 소문자는 엄연히 다른 코드다!

    SELECT *
        FROM ANIMAL_INS i
        WHERE UPPER(i.NAME) LIKE '%EL%'
    # upper 사용 왜냐면! el, EL, eL, El 일 수도 있으니까 4가지 커버를 다 해줄 함수 
    # 대문자 소문자는 엄연히 다른 코드다! 
    
    #내 풀이 
    SELECT ANIMAL_ID,NAME
    FROM ANIMAL_INS
    WHERE ANIMAL_TYPE = 'DOG' AND NAME like '%el%'
    ORDER BY NAME
    ;
    
    #혜민님 풀이 : 정규표현식 사용 
    SELECT ANIMAL_ID, NAME
    FROM ANIMAL_INS
    WHERE NAME REGEXP 'EL'
    AND ANIMAL_TYPE = 'Dog'
    ORDER BY NAME ASC

- 루시와 엘라 찾기

    SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
    FROM ANIMAL_INS
    WHERE NAME IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
    ORDER BY ANIMAL_ID
    ;
    # SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
    # FROM ANIMAL_INS
    # WHERE NAME = 'Lucy' OR NAME ='Ella' OR NAME ='Pickle' OR NAME ='Rogan'
    #     OR NAME ='Sabrina' OR NAME ='Mitty'
    # ORDER BY ANIMAL_ID
    # ;
    

# SQL EVERYDAY 9월 19일 미션

여러분 프로그래머스 7 days challenge로 몸이 좀 풀리셨나요.
우리, 시간이 열흘이나 있으니까 어려운거 한 번 도전해 볼까요...!! 😅

- [Challenges (HackerRank)](https://www.hackerrank.com/challenges/challenges/problem) 
HackerRank Difficulty: Medium
Hint. HAVING 절에서 서브쿼리를 잘 활용하세요. 서브쿼리 안에도 또 서브쿼리를 쓸 수 있어요.
- 판다스 lnner join 문제 풀기

# Pandas JOIN

- jupyter noetebook 실행
- [Pandas INNER JOIN](https://github.com/dataitgirls3/Teaching-Materials/blob/master/SQL%20%26%20Pandas%20INNER%20JOIN.ipynb)
    - 데이터 모델링 : 조인을 사용할 때 테이블간의 관계는 보통
    - 1:1 / **1:n** ex) 고객 한명당 여러개의 주문 / n:1/ m:n 이 있다.
    - 1:1은 조인이 필요 없고, m:n은 현업에서 지양하는 부분(만나지 않길..!)

        ```pandas
        order_orderDetails = orders.merge(orderDetails, how='inner', on='OrderID')
        ```

- 스칼라 2  → 파이썬 : 값 (a =2)
- 벡터 2345 한 줄로 표현되는 숫자 → a = [2,3,4]
- 매트릭스 : 행렬 → 테이블  컬럼 a/b
- 텐서 : 3차원
- [Pandas LEFT JOIN](https://github.com/dataitgirls3/Teaching-Materials/blob/master/SQL%20%26%20Pandas%20LEFT%20JOIN.ipynb)
- 데이터에서 =이 없는 얘들은 우리가 값을 입력해야하고, =이 있으면 Defalt 값이당
    - ex) by 는 입력해야하고, ascending=True는 기본값

# 오늘 배운 것

- FROM, WHERE절의 SQL 서브쿼리, LIKE, 텍스트 데이터를 다루는 여러 함수 `UPPER()`, `LOWER()`, `LEFT()`, `RIGHT()`, `SUBSTRING_INDEX()`
- Pandas JOIN
- 앞으로 진행 될 프로젝트 타임라인 공유 (데이터야놀자, 공공데이터 활용 데이터 분석)

# 9월 19일 오전수업

- SQL: [Challenges (HackerRank)](https://www.hackerrank.com/challenges/challenges/problem) 문제풀이와 HAVING절에서의 서브쿼리 사용, 중첩 서브쿼리 사용 설명
- [SQL DML(Data Manipulation Language)](http://pythonstudy.xyz/python/article/204-SQLite-%EC%82%AC%EC%9A%A9)