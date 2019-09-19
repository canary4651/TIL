# SQL/PANDAS_06

# SQL 해커랭크 풀이

- [Challenges (HackerRank)](https://www.hackerrank.com/challenges/challenges/problem)
- 문제 조건

    Julia asked her students to create some coding challenges. 

    Write a query to print the hacker_id, name, and the total number of challenges created by each student. 

    Sort your results by the total number of challenges in descending order.

    **If more than one student created the same number of challenges, then sort the result by hacker_id.** 

    **If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.**

    select hacker_id, count(*) as c
    FROM Challenges 
    GROUP BY hacker_id
    HAVING c =
        (SELECT max(cnt)
         FROM (select hacker_id, count(*) as cnt
               from challenges
               group by hacker_id) as a  # 위의 group by h.hacker_id 내용을 넣어준 거임
         )
    # 노트 필기 참고 
    # 유니언과 with 함수 작성해서 문제 풀어보기! 

- 그룹 바이에 들어간 컬럼은 셀렉트 절에도 들어가야 한다

# PANDAS inner join 풀이

# 비평

1. 임산부의 운동은 자연유산의 위험을 증가시키는 것으로 인식됩니다. 그러나 한 연구는 정기적으로 운동을 하는 임산부가 그렇지 않은 임산부보다 오히려 자연 유산을 할 가능성이 낮다는 것을 보였습니다. 이 연구결과를 비판적으로 평가해주세요. <출처 『통계학』 류근관>
    - 건강별/체격별/운동 강도별 등  운동을 하는 사람별로 그룹을 세분화 시켜서 조사해야 함
2. ['탈코 세대' 20대 여성, 화장·성형 안하고 자동차 샀다](https://news.v.daum.net/v/20190916060505440?f=m)

    이 기사에서 잘못 분석된 점을 찾아보세요. 먼저 기사 원문을 다 읽고 진행해주세요.

    기사는 젊은 여성들의 주 지출품목으로 여겼던 화장품, 미용실, 의류판매 등 '외모를 가꾸고 예쁜 옷을 고르는' 것과 관련된 카테고리에서 급격하게 매출이 하락하고, 자동차 구매와 소프트웨어 개발에 소비가 급격하게 증가하고 있음을 관찰하여 이를 '탈코르셋'을 뒷받침하는 증거로 사용하고 있습니다. 

    위의 통계는 20대 여성의 '탈코르셋'을 증명하기에 충분한가요? 위의 논리 전개에서 허점을 발견해주세요. 기자가 '탈코르셋'을 이야기하기 위해서 추가적으로 분석해야 할 부분이 있을까요? 기존의 논리 전개를 비판하고, 보완해야 할 점을 제안해보세요. 새로운 데이터를 제안하는 것도 환영합니다.

    -