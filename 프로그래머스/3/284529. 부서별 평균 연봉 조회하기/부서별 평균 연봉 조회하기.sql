-- 코드를 작성해주세요
select A.DEPT_ID
      ,A.DEPT_NAME_EN AS DEPT_NAME_EN
      ,ROUND(AVG(B.SAL),0) AS AVG_SAL
  from HR_DEPARTMENT A
      ,HR_EMPLOYEES B
where A.dept_id = B.dept_id
group by A.DEPT_ID, A.DEPT_NAME_EN
ORDER BY AVG_SAL DESC
;