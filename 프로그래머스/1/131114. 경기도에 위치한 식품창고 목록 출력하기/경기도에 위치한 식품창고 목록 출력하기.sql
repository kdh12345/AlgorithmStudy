-- 코드를 입력하세요
SELECT A.WAREHOUSE_ID
      ,A.WAREHOUSE_NAME
      ,A.ADDRESS
      ,NVL(A.FREEZER_YN,'N') AS FREEZER_YN
  FROM FOOD_WAREHOUSE A
WHERE SUBSTR(A.ADDRESS,1,3) = '경기도'