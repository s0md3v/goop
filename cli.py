import sys
import json

from goop import goop

green = '\033[92m'
white = '\033[97m'
yellow = '\033[93m'
end = '\033[0m'

cookie = '<your facebook cookie>'

for page in range(int(sys.argv[2])):
	result = goop.search(sys.argv[1], cookie, page=page, full=True)
	for each in result:
		print ('''%s%s\n%s%s\n%s%s%s\n''' % (green, result[each]['text'], yellow, result[each]['url'], white, result[each]['summary'], end))
