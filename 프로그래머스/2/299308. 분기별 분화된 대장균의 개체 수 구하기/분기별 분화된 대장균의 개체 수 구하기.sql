-- 코드를 작성해주세요
SELECT CASE WHEN SUBSTR(DATE_FORMAT(A.DIFFERENTIATION_DATE,'%Y-%m-%d'),6,2) >= '01'
             and SUBSTR(DATE_FORMAT(A.DIFFERENTIATION_DATE,'%Y-%m-%d'),6,2) < '04'
            then '1Q'
            WHEN SUBSTR(DATE_FORMAT(A.DIFFERENTIATION_DATE,'%Y-%m-%d'),6,2) >= '04'
             and SUBSTR(DATE_FORMAT(A.DIFFERENTIATION_DATE,'%Y-%m-%d'),6,2) < '07'
            then '2Q'
            WHEN SUBSTR(DATE_FORMAT(A.DIFFERENTIATION_DATE,'%Y-%m-%d'),6,2) >= '07'
             and SUBSTR(DATE_FORMAT(A.DIFFERENTIATION_DATE,'%Y-%m-%d'),6,2) < '10'
            then '3Q'
            else '4Q'
            end as QUARTER
        ,count(1) as ECOLI_COUNT
   FROM ECOLI_DATA A
   group by QUARTER
 order by QUARTER
 ;