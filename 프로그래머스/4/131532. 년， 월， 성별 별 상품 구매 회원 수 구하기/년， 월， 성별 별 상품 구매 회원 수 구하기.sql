-- 코드를 입력하세요
SELECT to_char(B.SALES_DATE,'yyyy') as YEAR
      ,case when to_char(B.SALES_DATE,'mm') < '10'
            then substr(to_char(B.SALES_DATE,'mm'),2,1)
            else to_char(B.SALES_DATE,'mm')
            end  as MONTH
      ,A.gender
      ,count(distinct B.user_id) as USERS
  FROM USER_INFO A
      ,ONLINE_SALE B
where A.USER_ID = B.USER_ID
  and A.gender in (0,1)
group by to_char(B.SALES_DATE,'yyyy') , to_char(B.SALES_DATE,'mm'), A.gender
order by to_char(B.SALES_DATE,'yyyy') , to_char(B.SALES_DATE,'mm'), A.gender