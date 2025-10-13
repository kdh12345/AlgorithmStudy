-- 코드를 입력하세요
SELECT A.MCDP_CD AS 진료과코드
      ,count(DISTINCT A.PT_NO) AS 5월예약건수
  from APPOINTMENT A
where YEAR(A.APNT_YMD) = 2022
  and month(A.APNT_YMD) = 05
group by A.MCDP_CD
order by 5월예약건수, 진료과코드
;