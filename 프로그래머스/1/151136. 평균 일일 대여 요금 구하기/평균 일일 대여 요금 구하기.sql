-- 코드를 입력하세요
SELECT floor(avg(DAILY_FEE)) AVERAGE_FEE
  from CAR_RENTAL_COMPANY_CAR
where car_type = 'SUV'
;