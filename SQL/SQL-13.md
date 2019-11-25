# SQL 13

# WINDOW FUNCTION

[https://mode.com/sql-tutorial/sql-window-functions](https://mode.com/sql-tutorial/sql-window-functions)

[http://www.gurubee.net/lecture/2382](http://www.gurubee.net/lecture/2382)

- hive (대용량 분산 처리 디비)
- presto
- 다 window fuction 지원 (mysql은 지원 안해서...불만이 많음)

    SELECT duration_seconds,
           SUM(duration_seconds) OVER (ORDER BY start_time) AS running_total
      FROM tutorial.dc_bikeshare_q1_2012
    
    # If you'd like to narrow the window from the entire dataset to individual groups within the dataset, 
    # you can use PARTITION BY to do so:
    
    SELECT start_terminal,
           duration_seconds,
           SUM(duration_seconds) OVER (PARTITION BY start_terminal ORDER BY start_time)
             AS running_total
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'
    
    # = 같은 뜻이지만 이렇게 돌리면 start_ternimal마다 값이 하나씩 나오지만, 위에 처럼 하면 row별로 붙여줌
    SELECT start_terminal,
           duration_seconds,
           SUM(duration_seconds) 
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'
    ORDER BY start_terminal 
    
    # 그럼 가능한 것 
    SELECT df.duration_seocds/ df.start_termianl_total
    FROM (
    SELECT start_terminal,
           duration_seconds,
           SUM(duration_seconds) OVER (PARTITION BY start_terminal ORDER BY start_time)
             AS running_total
    			 MAX(duration_seconds) OVER (PARTITION BY start_terminal ORDER BY start_time)
             AS running_total
    			 MIN(duration_seconds) OVER (PARTITION BY start_terminal ORDER BY start_time)
             AS running_total
    			 COUNT(duration_seconds) OVER (PARTITION BY start_terminal ORDER BY start_time)
             AS running_total
    			 AVG(duration_seconds) OVER (PARTITION BY start_terminal ORDER BY start_time)
             AS running_total
    				# SUM뿐만 아니라, max,min,count, avg 다 가능 
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'
    ) as df
    
    
    

# ROW_NUMBER()

    SELECT start_terminal,
           start_time,
           duration_seconds,
           ROW_NUMBER() OVER (ORDER BY start_time)
                        AS row_number
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'
    
    SELECT start_terminal,
           start_time,
           duration_seconds,
           ROW_NUMBER() OVER (PARTITION BY start_terminal
                              ORDER BY start_time)
                        AS row_number
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'

# RANK() and DENSE_RANK()

- If you order by start_time, for example, it might be the case that some terminals have rides with two identical start times. In this case, they are given the same rank, whereas ROW_NUMBER() gives them different numbers. In the following query, you notice the 4th and 5th observations for start_terminal 31000—they are both given a rank of 4, and the following result receives a rank of 6:
- row_number, rank, dense_rank 세개가 셋트고 차이가 있다는 것은 알기.
- row_number는 어떻게 해서든 1234568910 으로 매겨줌 (중복이여도
- rank는 4등을 동시에 줘서 5등없이 6등으로 스킵함
- 근데 dense_rank는 5등을 줌. (아주 근소한 차이지만 함수가 다르게 나옴)

    SELECT start_terminal,
           duration_seconds,
           RANK() OVER (PARTITION BY start_terminal
                        ORDER BY start_time)
                  AS rank
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'

- You can also use `DENSE_RANK()` instead of `RANK()` depending on your application. Imagine a situation in which three entries have the same value. Using either command, they will all get the same rank. For the sake of this example, let's say it's "2." Here's how the two commands would evaluate the next results differently:
    - `RANK()` would give the identical rows a rank of 2, then skip ranks 3 and 4, so the next result would be 5
    - `DENSE_RANK()` would still give all the identical rows a rank of 2, but the following row would be 3—no ranks would be skipped.

# NTILE

- -tile로 끝나면 데이터를 뭔가 selection으로 나눴구나 생각하면 됨
- ntile은 우리가 n을 설정할 수 있음

    SELECT start_terminal,
           duration_seconds,
           NTILE(4) OVER #파이션 안에서 데이터를 쪼게는데 그 기준이 duration_seocds로 하겠다는 뜻
             (PARTITION BY start_terminal ORDER BY duration_seconds)
              AS quartile,
           NTILE(5) OVER
             (PARTITION BY start_terminal ORDER BY duration_seconds)
             AS quintile,
           NTILE(100) OVER
             (PARTITION BY start_terminal ORDER BY duration_seconds)
             AS percentile # 100개로 끝나야하는 데, 데이터 개수가 작다면 그 전에 끝나버림
    											# 그러니까 partition 별로 데이터 개수를 확인하고 돌리자! *다른 ntile에서도 동일! 
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'
     ORDER BY start_terminal, duration_seconds

- sql 단점 : 일단 돌아감,,,그니까 막 하고 바로 보고 하지 말고 무조건 살펴보자 ^^

# LAG and LEAD

- lag lead : 내 데이터의 두번째 앞에 있는 거(lag), 뒤에 있는 거 가져와!(lead)
- **생각보다 진짜 많이 씀!!!!**

    SELECT start_terminal,
           duration_seconds,
           LAG(duration_seconds, 1) OVER #duration_seocds 앞에 있는 1개! 
             (PARTITION BY start_terminal ORDER BY duration_seconds) AS lag,
           LEAD(duration_seconds, 1) OVER
             (PARTITION BY start_terminal ORDER BY duration_seconds) AS lead
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'
     ORDER BY start_terminal, duration_seconds
    
    -- 배송 완료 할 때마다 버튼을 누르면, 이 집에서 배송을 완료하고 다음집에서 누르고 시간들이 딱딱 찍히면 그 다음 배송까지 시간이 줄여야 좋은 알고리즘. 
    -- 어떤 순서로 배송하게끔 만들 수 있음  
    
    SELECT start_terminal,
           duration_seconds,
           duration_seconds -LAG(duration_seconds, 1) OVER #duration에서 -lag 빼서 살펴보기
             (PARTITION BY start_terminal ORDER BY duration_seconds)
             AS difference
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'
     ORDER BY start_terminal, duration_seconds

# Defining a window alias

- window alias 모아 놓는 기능이 있는 db도 있다!

    SELECT start_terminal,
           duration_seconds,
           NTILE(4) OVER
             (PARTITION BY start_terminal ORDER BY duration_seconds)
             AS quartile,
           NTILE(5) OVER
             (PARTITION BY start_terminal ORDER BY duration_seconds)
             AS quintile,
           NTILE(100) OVER
             (PARTITION BY start_terminal ORDER BY duration_seconds)
             AS percentile
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'
     ORDER BY start_terminal, duration_seconds
    
    
    SELECT start_terminal,
           duration_seconds,
           NTILE(4) OVER ntile_window AS quartile,
           NTILE(5) OVER ntile_window AS quintile,
           NTILE(100) OVER ntile_window AS percentile
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'
    WINDOW ntile_window AS #alias 모아 놓기 
             (PARTITION BY start_terminal ORDER BY duration_seconds)
     ORDER BY start_terminal, duration_seconds