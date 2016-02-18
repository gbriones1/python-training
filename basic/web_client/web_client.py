import urllib2
import urllib
import json

info = {'foo':16, 'bar':50}

#data = urllib.urlencode(info)
#headers = {}

data = json.dumps(info)
headers = {'Content-Type': 'application/json'}

request = urllib2.Request('http://10.219.24.52:9000', data, headers)
response = urllib2.urlopen(request)
html = response.read()

print html
