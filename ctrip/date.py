# import datetime
# now = datetime.date.today()
# now_day_1 = now

# dates = {}

# for n_week in range(1):
#     dates[n_week] = [(now_day_1 + datetime.timedelta(days=d)).strftime("%y-%m-%d") for d in range(7)]
#     dates[n_week]=	[(now_day_1 + datetime.timedelta(mdasy[today.month])).]

# # print dates
# from calendar import mdays
# from datetime import datetime, timedelta

# today = datetime.now()
# next_month_of_today = today + timedelta(mdays[today.month])
# print next_month_of_today
from datetime import datetime
from dateutil.relativedelta import relativedelta
def date():
	today = datetime.now().date()
	dt=[];dt1=[];d=[];d1=[];final=[];
	for i in range(8):
	   dt.append(today + relativedelta(days=+i))
	d.append(tuple(t for t in zip(dt[::1], dt[1::1])))
	next_month = today + relativedelta(months=+1)
	for i in range(8):
	   dt1.append(next_month + relativedelta(days=+i))
	d1.append(tuple(t for t in zip(dt1[::1], dt1[1::1])))
	final = d+d1
	final = [k for i in final for k in i]
	return final

'''
import datetime
from dateutil import relativedelta
def date():
	nextmonth = []
	thismonth=[]
	thismonth = [datetime.date.today()+datetime.timedelta(days=d) for d in range(8)]
	nextmonth = [datetime.date.today()+datetime.timedelta(days=d) + relativedelta.relativedelta(months=1) for d in range(8)]
	#print type(str(nextmonth[0]))
	#print type(str(thismonth[0]))
		#c=[]
		#c = [tuple(zip(thismonth,thismonth[d] for d in range(1,7)))]
	d = [tuple(t for t in zip(thismonth[::1], thismonth[1::1]))]
	d.append(tuple(t for t in zip(nextmonth[::1], nextmonth[1::1])))
	res=[k for i in d for k in i]
	#print d
	return res'''

