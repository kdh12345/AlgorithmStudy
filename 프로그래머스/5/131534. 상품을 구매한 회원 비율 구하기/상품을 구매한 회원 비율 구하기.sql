-- 코드를 입력하세요
SELECT YEAR(B.SALES_DATE) AS YEAR
      ,MONTH(B.SALES_DATE) AS MONTH
      ,COUNT(DISTINCT(B.USER_ID)) AS PURCHASED_USERS
      ,ROUND(COUNT(DISTINCT(B.USER_ID)) / (SELECT COUNT(T.USER_ID)
                           FROM USER_INFO T
                         WHERE YEAR(T.JOINED) = '2021') ,1) AS PUCHASED_RATIO
  from USER_INFO A
      ,ONLINE_SALE B
WHERE A.USER_ID = B.USER_ID
  AND A.USER_ID IN (SELECT X.USER_ID
                      FROM USER_INFO X
                    WHERE YEAR(X.JOINED) = '2021')
GROUP BY YEAR(B.SALES_DATE)
      ,MONTH(B.SALES_DATE)
ORDER BY YEAR, MONTH
;