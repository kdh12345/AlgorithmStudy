-- 코드를 입력하세요
SELECT A.FOOD_TYPE
      ,A.REST_ID
      ,A.REST_NAME
      ,A.FAVORITES
  FROM REST_INFO A
WHERE (A.FOOD_TYPE,A.FAVORITES) IN (SELECT X.FOOD_TYPE
                                        ,MAX(X.FAVORITES)
                                   FROM REST_INFO X
                                 GROUP BY X.FOOD_TYPE
                                        )
ORDER BY A.FOOD_TYPE DESC
;