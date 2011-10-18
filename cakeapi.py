import urllib
import urllib2
try:
    import json
except ImportError:
    import simplejson as json

API_KEY = 'Your API Key Here'
API_URL = url='https://api.wbsrvc.com/%s/%s/'

def request(noun, verb, **params):
    headers = {'apikey' : API_KEY}
    body = php_encode(params)
    url = API_URL % (noun, verb)
    request = urllib2.Request(url, body, headers)
    response = json.loads(urllib2.urlopen(request).read())
    assert response['status'] == 'success', response
    return response['data']

def _flatten(d, parent):
    final = {}
    for k, v in d.items():
        if type(v) == dict:
            final.update(_flatten(v, parent='%s[%s]' % (parent, k)))
        else:
            if parent:
                final['%s[%s]' % (parent, k)] = v
            else:
                final[k] = v
    return final

def php_encode(data):
    parts = []
    for k, v in data.items():
        if type(v) == dict:
            parts.extend(_flatten(v, parent=k).items())
        else:
            parts.append((k, v))
    parts.sort()
    return urllib.urlencode(parts)
