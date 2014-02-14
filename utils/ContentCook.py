

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
				return params
	else:
		return None


def trimQuote(t):
	p = t.strip()
	if p[0] == '"' and p[len(p)-1] == '"':
		return p[1:len(p)-1]
	else:
		return p
