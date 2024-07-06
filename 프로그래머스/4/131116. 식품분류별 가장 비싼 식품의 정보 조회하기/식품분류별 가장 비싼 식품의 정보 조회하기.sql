-- 코드를 입력하세요
SELECT A.category
      ,A.price AS MAX_PRICE
      ,A.product_name
  from FOOD_PRODUCT A
where A.category in ('과자','국','김치','식용유')
  and (A.category,A.price) in (select X.category
                                     ,MAX(X.price)
                                 from FOOD_PRODUCT X
                               group by X.category)
order by MAX_PRICE DESC
;
                        