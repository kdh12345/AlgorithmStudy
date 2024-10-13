-- 코드를 입력하세요
SELECT A.MEMBER_NAME
      ,B.REVIEW_TEXT
      ,TO_CHAR(B.REVIEW_DATE,'YYYY-MM-DD') AS REVIEW_DATE
  FROM MEMBER_PROFILE A
      ,REST_REVIEW B
WHERE A.MEMBER_ID = B.MEMBER_ID
  AND A.MEMBER_ID IN (SELECT X.MEMBER_ID
                        FROM REST_REVIEW X
                     GROUP BY X.MEMBER_ID
                     HAVING COUNT(*) = ( SELECT MAX((COUNT(1)))
                                           FROM REST_REVIEW T
                                         GROUP BY T.MEMBER_ID
                                    )
                      )
ORDER BY REVIEW_DATE, REVIEW_TEXT
;