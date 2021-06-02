from datetime import datetime
from time import gmtime, strftime
week = ["Chủ nhật", "Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy"]

cur_time = datetime.now()
print(cur_time)
timestamp = cur_time.timestamp()
print(timestamp)
index = int(cur_time.strftime('%w'))
time = cur_time.strftime("{},%d tháng %m năm %y %H:%M:%S GMT+07:00").format(week[index])
print(time)
