from quoratz import quoratz
from datetime import datetime, timedelta

UPDATED = 'Updated'
UPDATED_LEN = 7
AM_PM = ('am', 'pm')
AGO = 'ago'
JUST_NOW = 'Just now'

MONTH = {
		'Jan' : 1,
		'Feb' : 2,
		'Mar' : 3,
		'Apr' : 4,
		'May' : 5,
		'Jun' : 6,
		'Jul' : 7,
		'Aug' : 8,
		'Sep' : 9,
		'Oct' : 10,
		'Nov' : 11,
		'Dec' : 12
		}

WEEKDAY = {
		'Mon' : 0,
		'Tue' : 1,
		'Wed' : 2,
		'Thu' : 3,
		'Fri' : 4,
		'Sat' : 5,
		'Sun' : 6
		}

def getTimeString(datestring):
	# like 'Just now'
	if datestring.find(JUST_NOW) > -1:
		return datetime.now(tz=quoratz()).date().isoformat()
	cut = datestring
	index_update = cut.find(UPDATED)
	# like "Updated XXX", remove the prefix
	if index_update == 0:
		cut = datestring[UPDATED_LEN+1:]
	elif index_update > 0:
		print 'should no be, log here'
		return None
	#like "xxx am" or "xxx pm"
	for temp in AM_PM:
		index_ap = cut.find(temp)
		if index_ap > -1:
			return handle_am_pm(cut, temp, index_ap)
	#like "xxx ago"
	if cut.find(AGO) > 0:
		return handle_ago(cut)
	#only week 
	if len(cut) == 3:
		return handle_week(cut) 
	return handle_dmy(cut)

def handle_am_pm(date, ap, index):
	hour_s = date[:index]
	hour_i = str2int(hour_s)
	if hour_i == -1:
		print "log here"
		return None
	elif ap == AM_PM[1] and hour_i <= 11:
		hour_i += 12
	now = datetime.now(tz=quoratz())
	then = now.replace(hour=hour_i)
	return then.date().isoformat()


def handle_ago(date):
	# 'xxh ago'
	index_h = date.find('h')
	if index_h > -1:
		hour_s = date[:index_h]
		hour_i = str2int(hour_s)
		if hour_i > -1:
			now = datetime.now(tz=quoratz())
			then = now + timedelta(hours=-hour_i)
			return then.date().isoformat()
		else:
			print 'log here'
			return None
	# 'xxm ago'
	index_m = date.find('m')
	if index_m > -1:
		minu_s = date[:index_m]
		minu = str2int(minu_s)
		if minu > -1:
			now = datetime.now(tz=quoratz())
			then = now + timedelta(minutes=-minu)
			return then.date().isoformat()
		else:
			print "should log here"
			return None

def handle_week(date):
	week = getDict(date, WEEKDAY)
	if week == -1:
		print 'log error'
		return None
	now = datetime.now(tz=quoratz())
	now_week = now.weekday()
	if now_week == week:
		return now.date().isoformat()
	elif now_week < week:
		print 'warning log here ,why?'
		return None
	else :
		then = now - timedelta(days=(now_week-week))
		return then.date().isoformat()
	
def handle_dmy(date):
	day_i = -1
	month_i = -1
	year_i = -1
	index_space = date.find(' ')
	if index_space > -1:
		day_s = date[:index_space]
		day_i = str2int(day_s)
		index_comma = date.find(',')
		if index_comma > -1:
			month_s = date[index_space+1 : index_comma]
			month_i = getDict(month_s, MONTH)	
			year_s = date[index_comma+1:]
			year_i = str2int(year_s)
			if day_i > -1 and month_i > -1 and year_i > -1:
				now = datetime.now(tz=quoratz())
				then = now.replace(year = year_i, day = day_i, month = month_i)
				return then.date().isoformat()
			else:
				print 'log here'
				return None
		else:
			month_s = date[index_space+1 :]
			month_i = getDict(month_s, MONTH)
			if day_i > -1 and month_i > -1:
				now = datetime.now(tz=quoratz())
				then = now.replace(day = day_i, month = month_i)
				return then.date().isoformat()
			else:
				print 'log here'
				return None
	else:
		print 'should log here'
		return None

def str2int(s):
	try:
		i = int(s)
		return i
	except:
		print 'cast error log here'
		return -1

def getDict(s, d):
	try:
		ret = d[s]
		return ret
	except:
		print 'dic key error'
		return -1
def test(s):
	print s, "|  ",getTimeString(s)

if __name__ == '__main__':
	#test("Updated 2am")
	#test("Mon")
	#test("Updated Tue")
	#test("11h ago")
	#test("6 Jan")
	#test("Updated 24 Dec")
	test("3 Dec, 2012")
	test("Updated 10 Dec, 2012")
	test("Updated 27 Dec")
	test("23 Sep")
	test("Mon")
	test("Updated 4h ago")
	test("4h ago")
	test("54m ago")


