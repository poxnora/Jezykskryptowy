import datetime

date = datetime.date(2010,12,12)
datenow = datetime.date.today()

e = datenow - date
print(e)