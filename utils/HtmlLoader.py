import urllib2
import URL
import ContentCook

def doFirstRequest(url):
	rq = urllib2.Request(url)
	setQuestionHeader(rq, url)
	content = urllib2.urlopen(rq)
	params = ContentCook.getLoadParams(content)
	if params != None:
		t = URL.URL4Load(url)
		t.buildDynamicURL(params)
		load_rq = urllib2.Request(t.getURL())
		setQuestLoadHeader(load_rq,t)
		print  urllib2.urlopen(load_rq).read()

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

def setQuestLoadHeader(rq, load):

	rq.add_header('Request','GET '+load.getRelative()+' HTTP/1.1')
	rq.add_header('Accept','application/javascript, */*;q=0.8')
	rq.add_header('Referer', load.getReferenceURL())
	rq.add_header('Accept-Language','zh-CN')
	rq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')
	rq.add_header('Host', load.getDomain(1))
	rq.add_header('DNT','1')
	rq.add_header("Connection",'Keep-Alive')



if __name__ == '__main__':
	doFirstRequest('http://www.quora.com/Facts-and-Trivia/Off-the-top-of-your-head-what-is-the-most-interesting-fact-you-know')
	

