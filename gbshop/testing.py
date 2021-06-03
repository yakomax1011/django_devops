
from datetime import datetime


date = datetime.now()
month = date.month

winter = {12, 1, 2}
spring = {3, 4, 5}
summer = {6, 7, 8}
fall = {9, 10, 11}

if month in winter:
    print('зимы')
if month in spring:
    print('весны')
if month in summer:
    print('лета')
if month in fall:
    print('осени')

