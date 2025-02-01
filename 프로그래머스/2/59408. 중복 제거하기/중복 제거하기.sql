-- 코드를 입력하세요
SELECT COUNT(DISTINCT A.NAME) as count
  FROM ANIMAL_INS A
where A.NAME IS NOT null
;