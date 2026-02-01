-- 코드를 입력하세요
SELECT TO_NUMBER(TO_CHAR(A.DATETIME,'HH24')) AS HOUR
      ,COUNT(1) AS count
  FROM ANIMAL_OUTS A
WHERE to_char(A.datetime,'HH24:MI') between '09:00' AND '19:59'
GROUP BY to_char(A.datetime,'HH24')
ORDER BY HOUR
;