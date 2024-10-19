-- 코드를 입력하세요
SELECT A.category
      ,sum(B.sales) as total_sales
  FROM BOOK A
      ,BOOK_SALES B
where A.BOOK_ID = B.BOOK_ID
  and TO_CHAR(B.SALES_DATE,'YYYYMM') = '202201'
group by A.category
order by A.category
;