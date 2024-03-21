-- 코드를 작성해주세요
select COUNT(1) AS FISH_COUNT
   from FISH_INFO A
       ,FISH_NAME_INFO B
where A.FISH_TYPE = B.FISH_TYPE
  and B.FISH_NAME in ('BASS', 'SNAPPER')
  ;