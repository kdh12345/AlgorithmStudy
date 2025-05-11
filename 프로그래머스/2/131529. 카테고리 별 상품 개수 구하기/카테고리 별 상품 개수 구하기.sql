-- 코드를 입력하세요
SELECT   SUBSTR(PRODUCT_CODE,1,2) as category
       , COUNT(1) as products
  FROM PRODUCT
GROUP BY SUBSTR(PRODUCT_CODE,1,2)
order by PRODUCT_CODE
;