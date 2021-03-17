from datetime import date

f_date = date(2021,3,11)
l_date = date(2021,3,16)

delta = l_date - f_date

print(delta.days)