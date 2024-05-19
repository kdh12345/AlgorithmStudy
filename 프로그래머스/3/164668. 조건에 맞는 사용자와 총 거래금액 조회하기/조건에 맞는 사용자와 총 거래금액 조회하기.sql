-- 코드를 입력하세요
SELECT a.USER_ID
      ,a.NICKNAME
      ,sum(b.price) as total_sales
  from USED_GOODS_USER a
      ,USED_GOODS_BOARD b
where a.USER_ID = b.WRITER_ID
  and b.status = 'DONE'
group by a.USER_ID
      ,a.NICKNAME
having sum(b.price) >= 700000
order by total_sales
;