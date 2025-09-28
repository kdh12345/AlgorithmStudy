-- 코드를 작성해주세요
select A.DEPT_ID
     , A.DEPT_NAME_EN
     , ROUND(AVG(B.SAL)) AS AVG_SAL
  from HR_DEPARTMENT A
        inner join HR_EMPLOYEES B
           on A.DEPT_ID = B.DEPT_ID
group by A.DEPT_ID, A.DEPT_NAME_EN
order by AVG_SAL DESC
;