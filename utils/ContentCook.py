import time



LOGIN = "new(require(\"login\").LoggedOutHomeHeaderInlineLogin"
LOGIN_HMAC = "t1cKg1QhQsYPCA"
CLOSE_HMAC = "SDBOAlZ0QOxIFX"
# Only available for lines with a pair of quotation marks
def trimQuote(line):
	index_s = line.find("\"")
	if index_s != -1:
		index_e = line[index_s+1:].find("\"")
		if index_e != -1:
			ret = line[index_s+1: index_e+index_s+1]
			return ret
	else: 
		return line
	
class PostData:

	def setFormKey(self,formkey):
		self.formkey = formkey
        def setPostKey(self,postkey):
		self.postkey = postkey
        def setServerCallUrl(self,serverCallUrl):
		self.serverCallUrl = serverCallUrl


class ParseError(Exception):
	def __init__(self):
		print "parse is not correct"

#to abstract necessary params from the first Page
class FirstQuestionPage:
	def __init__(self,content):
		count = 0
		self.postdata = PostData() 

		for line in content:
			#  http get params
			if line.find('require("tchannel_up").start') != -1:
				index_s = line.find('start(')
				index_e = line.find(');')
				if index_s != -1 and index_e != -1:
					sub =  line[len('start(')+index_s : index_e]
					params = sub.split(",")
					for i in range(len(params)):
						params[i] = trimQuote(params[i])
						self.params = params
					count+=1

			# http post 
			if line.find("serverCallUrl: ") != -1:
				self.postdata.setServerCallUrl(trimQuote(line))
				count+=1
			
			if line.find("formkey: ") != -1:
				self.postdata.setFormKey(trimQuote(line))
				count+=1

			if line.find("postkey: ") != -1:
				self.postdata.setPostKey(trimQuote(line))
				count+=1



		#hmac
		self.login_hmac = LOGIN_HMAC
		count+=1
		self.close_hmac = CLOSE_HMAC
		count+=1
	

		if count != 6:
			print count
			raise ParseError()


		


	def getLoadParams(self):
		return self.params

	def getFormkey(self):
		return self.postdata.formkey

	def getPostKey(self):
		return self.postdata.postkey
	
	def getServerCallUrl(self):
		return self.postdata.serverCallUrl
						


		


