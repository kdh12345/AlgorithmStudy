-- 코드를 입력하세요
SELECT DATE_FORMAT(T.SALES_DATE, '%Y-%m-%d') as SALES_DATE
      ,T.PRODUCT_ID
      ,T.USER_ID
      ,T.SALES_AMOUNT
  FROM (
        SELECT DATE_FORMAT(A.SALES_DATE, '%Y-%m-%d') SALES_DATE
              ,A.PRODUCT_ID
              ,A.USER_ID
              ,A.SALES_AMOUNT
          FROM ONLINE_SALE A
      WHERE YEAR(A.SALES_DATE) = '2022'
        AND MONTH(A.SALES_DATE) = '03'
      UNION
      SELECT   DATE_FORMAT(B.SALES_DATE, '%Y-%m-%d') SALES_DATE
              ,B.PRODUCT_ID
              ,NULL
              ,B.SALES_AMOUNT
          FROM OFFLINE_SALE B
      WHERE YEAR(B.SALES_DATE) = '2022'
        AND MONTH(B.SALES_DATE) = '03'
  ) T
  ORDER BY T.SALES_DATE, T.PRODUCT_ID, T.USER_ID
  ;