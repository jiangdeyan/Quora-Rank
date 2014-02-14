import random

HTTP = 'http://'
HTTPS = 'https://'

TCH = 'tch'
QUEST_URL_PART1 = '.tch.quora.com/up/'
QUEST_URL_PART2 = '/updates?min_seq='
QUEST_URL_PART3 = '&channel='
QUEST_URL_PART4_TIMEOUT = '&timeout=2000&callback=jsonp'
QUEST_URL_PART4 = '&callback=jsonp'

TEST = '1442a6f999678809a14506544'


class URLError(Exception):
	def __init__(self, url, reason):
		print url, " ", reason

class URLtool:
	def __init__(self, url):
		self._url = url
		if url[:len(HTTP)] == HTTP or url[:len(HTTPS)] == HTTPS:
			url = url.split('//')[1]
		if url.find('//') != -1 or url.find('\\') != -1:
			raise URLError(url, 'contain // or \\')
		self.domain = url.split('/')
	def getDomain(self,i):
		if i < len(self.domain):
			return self.domain[i]
		else:
			return None
	def getRelative(self):
		topD = self.domain[0]
		index = self._url.find(topD)
		if index == -1:
			raise URLError(self.url, 'getRelative error')
		return self._url[len(topD)+index:]

class URL4Load(URLtool):
	def __init__(self, url):
		self._refer_url = url
		
	def buildDynamicURL(self,params):
		i = random.randint(100000,999999)
		url = HTTP+TCH+str(i)+QUEST_URL_PART1+params[2]+QUEST_URL_PART2+params[0]+QUEST_URL_PART3+params[1]+QUEST_URL_PART4_TIMEOUT+TEST
		URLtool.__init__(self,url)

	def getReferenceURL(self):
		return self._refer_url
	def getURL(self):
		return self._url


if __name__ == '__main__':
	a = URLtool("http://www.quora.com/Facts-and-Trivia/Off-the-top-of-your-head-what-is-the-most-interesting-fact-you-know")
	print a.getDomain(99)
	print a.getRelative()
	

