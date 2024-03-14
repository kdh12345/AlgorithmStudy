-- 코드를 작성해주세요
select A.ID
      ,B.FISH_NAME
      ,A.LENGTH
  FROM FISH_INFO A
        INNER JOIN FISH_NAME_INFO B
           ON A.FISH_TYPE = B.FISH_TYPE
WHERE (A.FISH_TYPE, A.LENGTH) IN (SELECT X.FISH_TYPE
                                ,MAX(X.LENGTH)
                            FROM FISH_INFO X
                         GROUP BY X.FISH_TYPE)
;