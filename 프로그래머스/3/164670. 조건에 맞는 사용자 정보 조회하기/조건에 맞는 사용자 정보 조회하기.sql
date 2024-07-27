-- 코드를 입력하세요
SELECT distinct(A.USER_ID) as USER_ID
      ,A.NICKNAME
      ,A.CITY || ' ' || A.STREET_ADDRESS1 || ' ' || A.STREET_ADDRESS2 AS 전체주소
      ,SUBSTR(A.TLNO,1,3) || '-' || SUBSTR(A.TLNO,4,4) || '-' || SUBSTR(A.TLNO,8,4) AS 전화번호
  from USED_GOODS_USER A
      ,USED_GOODS_BOARD B
WHERE A.USER_ID = B.WRITER_ID
  AND B.WRITER_ID IN (SELECT X.WRITER_ID
                       FROM USED_GOODS_BOARD X
                     GROUP BY X.WRITER_ID
                     HAVING COUNT(X.WRITER_ID) >= 3
                      )
ORDER BY A.USER_ID DESC
;