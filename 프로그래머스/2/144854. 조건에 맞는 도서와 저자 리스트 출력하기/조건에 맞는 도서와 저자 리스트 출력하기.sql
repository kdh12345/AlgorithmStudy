-- 코드를 입력하세요
SELECT A.BOOK_ID
      ,B.AUTHOR_NAME
      ,date_format(A.PUBLISHED_DATE,'%Y-%m-%d') AS PUBLISHED_DATE
  from BOOK A
      ,AUTHOR B
where A.author_id = B.author_id
  and A.CATEGORY = '경제'
order by PUBLISHED_DATE