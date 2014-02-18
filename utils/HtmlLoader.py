import urllib2
import URL
import ContentCook
from ContentCook import FirstQuestionPage

def doFirstRequest(url):
	rq = urllib2.Request(url)
	setFirstQuestionHeader(rq, url)
	content = urllib2.urlopen(rq,timeout=50000)
	#f = open('1') 
	#content = f
	print content.info()
	#print 
	#print content.info()['Set-Cookie']
	fqp = FirstQuestionPage(content)
	params = fqp.getLoadParams()
	print params
	if params != None and params >= 3:
		t = URL.URL4Load(url,params)
		load_rq = urllib2.Request(t.getURL())
		setQuestLoadHeader(load_rq,t)
		#print load_rq.header_items()
		#print  urllib2.urlopen(load_rq).read()

def setFirstQuestionHeader(rq, url):
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
	rq.add_header('Host', load.getDomain(0))
	rq.add_header('DNT','1')
	rq.add_header('Connection','Keep-Alive')
	#rq.add_header('Accept-Encoding','gzip, deflate')


def setPostRequest(rq, post, length):

	rq.add_header('Request','POST '+post.getRelative()+' HTTP/1.1')
	rq.add_header('Accept', 'application/json, text/javascript, */*; q=0.01')
	rq.add_header('Content-Type', 'application/x-www-form-urlencoded')
	rq.add_header('X-Requested-With','XMLHttpRequest')
	rq.add_header('Referer', post.getReferenceURL())
	rq.add_header('Accept-Language','zh-CN')
	rq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')
	rq.add_header('Host',post.getDomain(0))
	rq.add_header('Content-Length', str(length))
	rq.add_header('DNT','1')
	rq.add_header('Connection','Keep-Alive')
	rq.add_header('Cache-Control','no-cache')





if __name__ == '__main__':
	doFirstRequest('http://www.quora.com/Facts-and-Trivia/Off-the-top-of-your-head-what-is-the-most-interesting-fact-you-know')
	

