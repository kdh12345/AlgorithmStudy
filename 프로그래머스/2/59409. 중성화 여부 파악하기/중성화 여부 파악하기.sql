-- 코드를 입력하세요
SELECT A.ANIMAL_ID
      ,A.NAME
      ,CASE WHEN A.SEX_UPON_INTAKE like '%Neutered%' or A.SEX_UPON_INTAKE like '%Spayed%'
            then 'O'
            else 'X'
            end AS 중성화
  from ANIMAL_INS A
ORDER BY A.ANIMAL_ID
;
;