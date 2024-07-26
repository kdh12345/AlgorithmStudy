-- 코드를 입력하세요
SELECT A.ANIMAL_ID
      ,A.NAME
  FROM ANIMAL_INS A
WHERE A.ANIMAL_TYPE = 'Dog'
  and (A.NAME LIKE '%el%'
        OR A.NAME LIKE '%EL%'
       )
ORDER BY A.NAME
;