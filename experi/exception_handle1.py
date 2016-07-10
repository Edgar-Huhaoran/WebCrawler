from urllib2 import Request, urlopen, URLError, HTTPError

req = Request('http://bbs.csdn.net/noExist')

try:
    response = urlopen(req)

except HTTPError, e:
    print 'The server couldn\'t fulfill the request.'
    print e

except URLError, e:
    print 'We failed to reach a server.'
    print e

else:
    print 'No exception raised'
