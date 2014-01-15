from datetime import time, tzinfo, timedelta, datetime

#UTC-8 to UTC offset
QROFFSET = timedelta(hours=-8)
#DST default hour offset
DSTOFFSET = timedelta(hours=1)
# Zero offset
ZEROOFFSET = timedelta(hours=0)
# U.S DST on/off hour delta
USOFFSET = timedelta(hours=2)
#Local timezone(UTC+8) to UTC offset
LOCALOFFSET = timedelta(hours=8)

class quoratz(tzinfo):
	"""Quora server is in U.S. Silicon Valley, the timezone is UTC-8. Quora is public in 2010, so I use 2007 U.S. DST rules. Please refer to wikipedia"""
	def __init__(self):
		self.dstname = 'Quora timezone'
	def utcoffset(self, dt):
		return QROFFSET+self.dst(dt)
	def dst(self, dt):
		# DST ON TIME
		d = datetime(dt.year, 3, 14)
		wd = d.weekday()
		delta = ZEROOFFSET
		if wd == 6:
			delta = ZEROOFFSET+USOFFSET
		else:
			delta = USOFFSET-timedelta(days=wd+1)
		self.dston = d + delta
		# DST OFF TIME
		d = datetime(dt.year, 11, 7)
		wd = d.weekday()
		if wd == 6:
			delta = ZEROOFFSET+USOFFSET
		else:
			delta = USOFFSET-timedelta(days=wd+1)
		self.dstoff = d + delta
		# which offset
		if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
			return DSTOFFSET
		else:
			return ZEROOFFSET
	def tzname(self, dt):
		return self.dstname

class UTC(tzinfo):
	"""UTC timezone"""
	def __init__(self):
		self.dstname = "UTC"
	def utcoffset(self, dt):
		return -LOCALOFFSET
	def dst(self, dt):
		return ZEROOFFSET
	def tzname(self, dt):
		return self.dstname

class LocalTZ(tzinfo):
	"""Local timezone"""
	def __init__(self):
		self.dstname = "Local timezone"
	def utcoffset(self, dt):
		return ZEROOFFSET
	def dst(self, dt):
		return ZEROOFFSET
	def tzname(self, dt):
		return self.dstname

if __name__ == '__main__':
	d = datetime.now()
	d1 = d.replace(tzinfo=LocalTZ())
	d2 = d1.astimezone(UTC())
	dx = datetime.now(tz=quoratz())
	d3 = dx.astimezone(quoratz())
	#d4 = d1.astimezone(None)
	print "local time ", d1.strftime("%A, %d. %B %Y %I:%M%p")
	print "UTC time ", d2.strftime("%A, %d. %B %Y %I:%M%p")
	print "U.S. time ", dx.strftime("%A, %d. %B %Y %I:%M%p")

