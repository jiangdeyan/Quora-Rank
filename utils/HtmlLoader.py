import urllib2
import URL



def doRequest(url):
	rq = urllib2.Request(url)
	setQuestionHeader(rq, url)
	content = urllib2.urlopen(rq);
	getLoadParams(content)


def setQuestionHeader(rq, url):
	t = URL.URLtool(url)
	r = t.getRelative()
	rq.add_header('Request','GET '+r+' HTTP/1.1')
	rq.add_header('Accept','text/html, application/xhtml+xml, */*')
	rq.add_header('Accept-Language','zh-CN')
	rq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')
	#rq.add_header('Accept-Encoding','gzip, deflate')
	rq.add_header('Host','www.quora.com')
	rq.add_header('DNT','1')
	rq.add_header("Connection",'Keep-Alive')


def getLoadParams(content):
	for line in content:
		if line.find('require("tchannel_up").start') != -1:
			index_s = line.find('start(')
			index_e = line.find(');')
			if index_s != -1:
				sub =  line[len('start(')+index_s : index_e]
				params = sub.split(",")
				for i in range(len(params)):
					params[i] = trimQuote(params[i])
				print params


def trimQuote(t):
	p = t.strip()
	if p[0] == '"' and p[len(p)-1] == '"':
		return p[1:len(p)-1]
	else:
		return p

				
	


		



if __name__ == '__main__':
	doRequest('http://www.quora.com/Facts-and-Trivia/Off-the-top-of-your-head-what-is-the-most-interesting-fact-you-know')
	
