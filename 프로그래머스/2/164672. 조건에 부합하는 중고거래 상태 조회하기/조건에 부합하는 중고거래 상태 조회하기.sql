-- 코드를 입력하세요
SELECT A.BOARD_ID
      ,A.WRITER_ID
      ,A.TITLE
      ,A.PRICE
      ,CASE WHEN A.STATUS = 'SALE'
            THEN '판매중'
            WHEN A.STATUS = 'RESERVED'
            THEN '예약중'
            ELSE '거래완료'
            END AS 'STATUS'
  FROM USED_GOODS_BOARD A
WHERE YEAR(CREATED_DATE) = '2022'
  AND MONTH(CREATED_DATE) = '10'
  AND DAY(CREATED_DATE) = '05'
ORDER BY A.BOARD_ID DESC
;
            