-- 코드를 입력하세요
/*
SELECT a.member_name member_name
      ,b.review_text review_text
      ,TO_CHAR(b.review_date,'YYYY-MM-DD') review_date
  from member_profile a
      ,rest_review b
where a.member_id = b.member_id
  and a.member_id = (select t.member_id
                     FROM (select x.member_id member_id
                       from rest_review x
                    group by x.member_id
                    order by count(x.member_id) desc) t
                    where rownum <= 1)
order by REVIEW_DATE asc, REVIEW_TEXT
*/
select a.member_name member_name
      ,b.review_text review_text
      ,TO_CHAR(b.review_date,'YYYY-MM-DD') review_date
  from member_profile a
      ,rest_review b
where a.member_id = b.member_id
  and a.member_id in (select member_id
                        from rest_review
                      group by member_id
                     having count(*) = (
                        select max(count(*))
                          from rest_review
                        group by member_id
                     
                     )
                     )
order by b.review_date, review_text
;