import time
import math 



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

    return sign + base36

# Only available for lines with a pair of quotation marks
def trimQuote(line):
	if index_s != -1:
		index_e = line[index_s+1:].find("\"")
		if index_e != -1:
			ret = line[index_s+1: index_e+index_s+1]
			return ret
	


#to abstract necessary params from the first Page
class FirstQuestionPage:
	def __init__(self,content):
		for line in content:
			if line.find('require("tchannel_up").start') != -1:
				index_s = line.find('start(')
				index_e = line.find(');')
				if index_s != -1:
					sub =  line[len('start(')+index_s : index_e]
					params = sub.split(",")
					for i in range(len(params)):
						params[i] = trimQuote(params[i])
						self.params = params
			if line.find("serverCallUrl: ") != -1:
				self.serverCallUrl = trimQuote(line)
						
		else:
			return None


		


