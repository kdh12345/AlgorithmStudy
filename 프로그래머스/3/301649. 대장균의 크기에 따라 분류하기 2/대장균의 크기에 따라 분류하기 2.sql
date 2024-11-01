-- 코드를 작성해주세요
SELECT T.ID
      ,CASE WHEN T.R <= MAX_ID*0.25
            THEN 'CRITICAL'
            WHEN T.R <= MAX_ID*0.5
            THEN 'HIGH'
            WHEN T.R <= MAX_ID*0.75
            THEN 'MEDIUM'
            ELSE 'LOW'
            END AS COLONY_NAME
  FROM (SELECT A.ID
      ,ROW_NUMBER() OVER(ORDER BY SIZE_OF_COLONY DESC) AS R
      ,MAX(ID) OVER() AS MAX_ID
  FROM ECOLI_DATA A
 ) T
ORDER BY T.ID
 ;