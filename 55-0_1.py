import urllib.request
import urllib.parse

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data = {}
data['type'] = 'AUTO'
data['i'] = 'sha'
data['client'] = 'fanyideskweb'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')

print(html)
