-- 코드를 입력하세요
SELECT A.REST_ID
      ,A.REST_NAME
      ,A.FOOD_TYPE
      ,A.FAVORITES
      ,A.ADDRESS
      ,ROUND(AVG(B.REVIEW_SCORE),2) AS SCORE
  from rest_info A
      ,rest_review B
where A.REST_ID = B.REST_ID
  AND SUBSTR(A.ADDRESS,1,2) = '서울'
GROUP BY A.REST_ID
      ,A.REST_NAME
      ,A.FOOD_TYPE
      ,A.FAVORITES
      ,A.ADDRESS
ORDER BY SCORE DESC, A.FAVORITES DESC
;