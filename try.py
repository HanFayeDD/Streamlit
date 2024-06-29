import datetime

date = datetime.date(2024, 1, 1)
date_str = date.strftime("%Y%m%d")
print(date_str)
date_str = "20224-01-01"
formatted_date_str = date_str.replace("-", "")
print(formatted_date_str)
