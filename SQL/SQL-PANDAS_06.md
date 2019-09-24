# SQL/PANDAS_06

# SQL 해커랭크 풀이

- [Challenges (HackerRank)](https://www.hackerrank.com/challenges/challenges/problem)
- 문제 조건

    Julia asked her students to create some coding challenges. 

    Write a query to print the hacker_id, name, and the total number of challenges created by each student. 

    Sort your results by the total number of challenges in descending order.

    **If more than one student created the same number of challenges, then sort the result by hacker_id.** 

    **If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.**

    ```sql
    select hacker_id, count(*) as c
    FROM Challenges 
    GROUP BY hacker_id
    HAVING c =
        (SELECT max(cnt)
         FROM (select hacker_id, count(*) as cnt
               from challenges
               group by hacker_id) as a  # 위의 group by h.hacker_id 내용을 넣어준 거임
         )
    ```
    # 노트 필기 참고 
    # 유니언과 with 함수 작성해서 문제 풀어보기! 

- 그룹 바이에 들어간 컬럼은 셀렉트 절에도 들어가야 한다

# PANDAS inner join 풀이

