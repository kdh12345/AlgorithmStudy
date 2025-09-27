-- 코드를 입력하세요
SELECT A.CATEGORY
      ,SUM(B.SALES) AS TOTAL_SALES
  from BOOK A
      ,BOOK_SALES B
where A.BOOK_ID = B.BOOK_ID
   and YEAR(B.SALES_DATE) = 2022
  and MONTH(B.SALES_DATE) = '01'
group by A.CATEGORY
order by 1
;