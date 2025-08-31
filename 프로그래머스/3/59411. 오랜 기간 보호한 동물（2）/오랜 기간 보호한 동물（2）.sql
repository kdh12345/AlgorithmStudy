-- 코드를 입력하세요
SELECT T.ANIMAL_ID
       ,T.NAME
  FROM (SELECT  A.ANIMAL_ID
             ,A.NAME
             ,B.DATETIME - A.DATETIME as diff
  FROM ANIMAL_INS A
      ,ANIMAL_OUTS B
where A.ANIMAL_ID = B.ANIMAL_ID
group by A.ANIMAL_ID
        ,A.NAME
        ,B.DATETIME - A.DATETIME
order by diff desc
) T
WHERE ROWNUM <= 2
;