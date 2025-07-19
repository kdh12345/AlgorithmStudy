-- 코드를 입력하세요
SELECT A.animal_type
      ,nvl(A.NAME,'No name') AS NAME
      ,A.SEX_UPON_INTAKE
  from ANIMAL_INS A
order by A.animal_id
;