-- 코드를 작성해주세요
SELECT (
        CASE
            WHEN (SKILL_CODE & (select sum(code) from skillcodes where category like 'Front%'))
            and skill_code & (select CODE from skillcodes where NAME = 'Python')
            then 'A'
            when SKILL_CODE & (SELECT CODE FROM SKILLCODES where NAME = 'C#')
            then 'B'
            when SKILL_CODE & (SELECT sum(code) FROM SKILLCODES where category like 'Front%')
            then 'C'
            ELSE NULL
            end
) AS GRADE
    ,ID
    ,EMAIL
from DEVELOPERS
group by GRADE, ID, EMAIL
HAVING GRADE IS NOT NULL
ORDER BY GRADE, ID
;