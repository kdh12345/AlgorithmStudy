-- 코드를 입력하세요
SELECT *
  FROM FOOD_PRODUCT A
WHERE A.PRICE = (SELECT MAX(X.PRICE)
                        FROM FOOD_PRODUCT X
                )
                      ;