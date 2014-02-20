import urllib2
import urllib
import URL
import ContentCook
import math
import time
from ContentCook import FirstQuestionPage

#make convert python timestamp to js style. Just fake it
def getTimeStamp():
	return int(math.floor(time.time()*1e3))

#encode base on 36 radix
def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """Converts an integer to a base36 string."""
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')

    base36 = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36.lower()

def getE2eActionID():
	return base36encode(getTimeStamp()*int(1e3))

def doFirstRequest(url):
	#First request
	content = None
	try:
		rq = urllib2.Request(url)
		setFirstQuestionHeader(rq, url)
		content = urllib2.urlopen(rq,timeout=50000)
	except Exception as ret:
		print ret

	if content != None and content.getcode() == 200:
		fqp = FirstQuestionPage(content)
		content.read()
		post1 = URL.URL4Post(url,fqp.postdata.serverCallUrl)
		post_rq1 = urllib2.Request(post1.getURL())
		print post1.getURL()
		setPostRequest(post_rq1, post1, fqp.postdata, '387', 1)
		print post_rq1.header_items()
		print post_rq1.get_data()
		try:
			print urllib2.urlopen(post_rq1)
		except Exception as ret:pass
			#print ret

		post2 = URL.URL4Post(url,fqp.postdata.serverCallUrl)
		post_rq2 = urllib2.Request(post2.getURL())
		setPostRequest(post_rq2, post2, fqp.postdata, '903', 2)
		print post_rq2.header_items()
		print post_rq2.get_data()
		try:
			print urllib2.urlopen(post_rq2)
		except Exception as ret:
			print ret
											                        #print ret



		params = fqp.getLoadParams()
		if params != None and params >= 3:
			t = URL.URL4Load(url,params)
			load_rq = urllib2.Request(t.getURL())
			setQuestLoadHeader(load_rq,t)
			#print load_rq.header_items()
			print  urllib2.urlopen(load_rq).read()

def setFirstQuestionHeader(rq, url):
	rq.add_header('Accept','text/html, application/xhtml+xml, */*')
	rq.add_header('Accept-Language','zh-CN')
	rq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')
	#rq.add_header('Accept-Encoding','gzip, deflate')
	rq.add_header('Host','www.quora.com')
	rq.add_header('DNT','1')
	#rq.add_header("Connection",'Keep-Alive')
	rq.add_header("Connection",'close')

def setQuestLoadHeader(rq, load):

	rq.add_header('Accept','application/javascript, */*;q=0.8')
	rq.add_header('Referer', load.getReferenceURL())
	rq.add_header('Accept-Language','zh-CN')
	rq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')
	rq.add_header('Host', load.getDomain(0))
	rq.add_header('DNT','1')
	rq.add_header('Connection','Keep-Alive')
	#rq.add_header('Accept-Encoding','gzip, deflate')

POST_11 = 'json=%7B%22args%22%3A%5B%5D%2C%22kwargs%22%3A%7B%22email%22%3A%22%22%7D%7D&formkey='
POST_12 = '&postkey='
POST_13 = '&window_id='
POST_14 = '&referring_controller=question&referring_action=q&__vcon_json=%5B%22hmac%22%2C%22'
POST_15 = '%22%5D&__vcon_method=preview_info&__e2e_action_id='
POST_16 = '&__first_server_call=true&js_init=%7B%7D'

POST_21 = 'json=%7B%22args%22%3A%5B%5D%2C%22kwargs%22%3A%7B%22step_name%22%3A%22signup_dialog_begin%22%7D%7D&formkey='
POST_22 = '&postkey='
POST_23 = '&window_id='
POST_24 = '&referring_controller=question&referring_action=q&__vcon_json=%5B%22hmac%22%2C%22'
POST_25 = '%22%5D&__vcon_method=record_step&__e2e_action_id='
POST_26 = '&js_init=%7B%22show_google_connect%22%3Atrue%2C%22show_facebook_connect%22%3Atrue%2C%22code%22%3Anull%2C%22has_passwordless%22%3Afalse%2C%22auth_explanation_subtitle%22%3A%22We+won\'t+store+your+password+or+spam+you+or+your+friends.%22%2C%22show_explanation%22%3Atrue%2C%22auth_explanation_title%22%3A%22You+must+sign+in+to+read+past+the+first+answer.%22%2C%22nux_url%22%3A%22%2Fhome%2Fwelcome%22%2C%22background_click_dismisses_dialog%22%3Atrue%2C%22show_twitter_connect%22%3Afalse%2C%22enable_passwordless_signup%22%3Atrue%2C%22disable_background_close_on_connect%22%3Atrue%7D'

def setPostRequest(rq, post, postdata, length, i):

	rq.add_header('Accept', 'application/json, text/javascript, */*; q=0.01')
	rq.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
	rq.add_header('X-Requested-With','XMLHttpRequest')
	rq.add_header('Referer', post.getReferenceURL())
	rq.add_header('Accept-Language','zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3')
	rq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0')
	rq.add_header('Host',post.getDomain(0))
	rq.add_header('Content-Length', str(length))
	rq.add_header('DNT','1')
	rq.add_header('Connection','Keep-Alive')
	rq.add_header('Cache-Control','no-cache')
	rq.add_header('Accept-Encoding','gzip, deflate')
	rq.add_header('Cookie','m-s=\"hZ2gQVXwpeYgF_vheNcQow\075\075\"; __utmc=261736717; m-b=\"7j3LvTY0vgxzgUmsKD6pDQ\075\075\"; m-tz=-480')

	data = ''
	if i == 1:
		data = POST_11+postdata.formkey+POST_12+postdata.postkey+POST_13+postdata.windowId+POST_14+postdata.login_hmac+POST_15+getE2eActionID()+POST_16
	elif i == 2:
		data = POST_21+postdata.formkey+POST_22+postdata.postkey+POST_23+postdata.windowId+POST_24+postdata.close_hmac+POST_25+getE2eActionID()+POST_26
	rq.add_data(data)
	#setData(rq,postdata)
	#return data


def setData(rq, postdata):
	data = {
			'__e2e_action_id' : str(getE2eActionID()),
			'__first_server_call' : 'true',
			'__vcon_json' : '[\"hmac\",\"t1cKg1QhQsYPCA\"]',
			'__vcon_method' : 'preview_info',
			'formkey' : postdata.formkey,
			'js_init' : '{}',
			'json' : '{\"args\":[],\"kwargs\":{\"email\":\"\"}}',
			'postkey' : postdata.postkey,
			'referring_action' : 'q',
			'referring_controller' : 'question',
			'window_id' : postdata.windowId
			}
	rq.add_data(urllib.urlencode(data))




if __name__ == '__main__':
	doFirstRequest('http://www.quora.com/Facts-and-Trivia/Off-the-top-of-your-head-what-is-the-most-interesting-fact-you-know')
	

