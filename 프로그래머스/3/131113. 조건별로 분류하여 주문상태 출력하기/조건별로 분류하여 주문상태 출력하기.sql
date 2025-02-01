-- 코드를 입력하세요
SELECT A.ORDER_ID
      ,A.PRODUCT_ID
      ,to_char(A.OUT_DATE,'YYYY-MM-DD') as OUT_DATE
      ,case when to_char(A.OUT_DATE,'YYYYMMDD') <= '20220501'
            then '출고완료'
            when A.OUT_DATE IS NULL
            then '출고미정'
            else '출고대기'
            end as 출고여부
  from FOOD_ORDER A
order by A.ORDER_ID
;