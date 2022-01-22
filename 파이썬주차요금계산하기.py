from datetime import datetime
from math import ceil


def calc_fee(fees, parking_time):
    if parking_time <= fees[0]:
        return fees[1]
    else:
        return fees[1] + fees[3] * ceil((parking_time - fees[0]) / fees[2])


def solution(fees,records):
    car_records = {}
    for record in records[::-1]:
        t_in_out, car_num, in_out = record.split(' ')
        car_records.setdefault(car_num,{'parking_time': 0})
        if in_out == 'OUT':
            car_records[car_num]['out_time'] = datetime.strptime(t_in_out,'%H:%M')
        else:
            if not car_records[car_num].get('out_time'):
                car_records[car_num]['out_time'] = datetime.strptime('23:59', '%H:%M')
            car_records[car_num]['parking_time'] += (car_records[car_num]['out_time'] - datetime.strptime(t_in_out,'%H:%M')).seconds//60
    return [calc_fee(fees,car_records[car_num]['parking_time']) for car_num in sorted(car_records.keys())]