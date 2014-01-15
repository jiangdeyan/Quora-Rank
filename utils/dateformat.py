from quoratz import quoratz

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
		'Dec' : 12,
		}

WeekDay = {
		'Mon' : 0
		'Tue' : 1
		'Wed' : 2
		'Thu' : 3
		'Fri' : 4
		'Sat' : 5
		'Sun' : 6
		}

def getTimeString(datestring):

	# like 'Just now'
	if datestring.find(JUST_NOW):
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
			return handle_am_pm(cut,ap,index_ap)
	#like "xxx ago"
	if cut.find(AGO) > 0:
		return handle_ago(cut)
	#only week 
	if len(cut) == 3:
		return handle_week(cut) 
	return handle

def handle_am_pm(date, ap, index):
	hour = -1
	hour_s = date[:index]
	try:
		hour = int(hour_s)
		if ap == AM_PM[1] and ap <= 11:
			hour += 12
		now = datetime.now(tz=quoratz())
		then = now.replace(hour=hour)
		return then.date().isoformat()
	except:
		print 'should log here'
		return None


def handle_ago(date):
	index_h = date.find('h')
	if index_h > -1:
		hour_s = date[:index_h]
		try:
			hour = int(hour_s)
			assert hour > 0
			now = datetime.now(tz=quoratz())
			then = now + timedelta(hour=-hour)
			return then.date().isoformat() 
		except:
			print "should log here"
			return None
	index_m = date.find('m')
	if index_m > -1:
		minu_s = date[:index_m]
		try:
			minu = int(minu_s)
			now = datetime.now(tz=quoratz())
			then = now + timedelta(minute=-minu)
			return then.date().isoformat()
		except:
			print "should log here"
			return None

def handle_week(date):
	week = -1
	try:
		week = WeekDay[date]
	except:
		print 'should log here'
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
		try:
			day_i = int(day_s)
		except:
			print 'log here'
			return None
		index_comma = date.find(',')
		if index_comma > -1:
			month_s = date[index_space+1 : index_comma]
			try:
				mouth_i = MONTH[month_s]
			except:
				print 'log here'
				return None
			year_s = date[index_comma:]
			try:
				year_i = int(year_s)
				if day_i > -1 and month_i > -1 and year_i > -1
				now = datetime.now(tz=quoratz())
				then = now.replace(day = day_i, month = month_i)
			except:
				print 'log here'
				return None
			
		else:
			now = datetime.now(tz=quoratz())
			if day_i > -1 and month_i > -1:
				then = now.replace(day = day_i, month = month_i)
				return then.date().isoformat()
			else:
				print 'log here'
				return None
	else:
		print 'should log here'
		return None






