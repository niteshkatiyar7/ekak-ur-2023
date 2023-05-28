import datetime
now = datetime.now()
print(now.strftime("%H:%M:%S"), hash(now.strftime("%H:%M:%S")))
