-- 코드를 작성해주세요
select COUNT(*) AS FISH_COUNT
      ,B.FISH_NAME 
   from FISH_INFO A
       ,FISH_NAME_INFO B
where A.FISH_TYPE = B.FISH_TYPE
GROUP BY B.FISH_TYPE, B.FISH_NAME
ORDER BY 1 DESC
;