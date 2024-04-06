-- 코드를 작성해주세요
select ii.item_id
      ,ii.item_name
      ,ii.rarity
  from item_info ii
      ,item_tree it
where ii.item_id = it.item_id
  and it.item_id not in (
                        select x.parent_item_id
                          from item_tree x
                        where parent_item_id is not null
                        group by parent_item_id
  )
  order by ii.item_id desc;