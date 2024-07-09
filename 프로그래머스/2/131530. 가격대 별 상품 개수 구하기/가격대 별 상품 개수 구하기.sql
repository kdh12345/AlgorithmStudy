-- 코드를 입력하세요
SELECT FLOOR(PRICE/10000)*10000 as PRICE_GROUP
      ,count(1) as products
  from PRODUCT
group by FLOOR(PRICE/10000)*10000
order by PRICE_GROUP
;