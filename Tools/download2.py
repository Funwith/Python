import urllib
import requests
download = urllib.URLopener()
for i in range(1,200):
	url = 'http://streamServer.io' + str(i) # changed
	if requests.get(url).headers['content-type'] == 'video/mp4':
		print 'Complete: ' + url + '.mp4'
		download.retrieve(url,str(i) + '.mp4')
	else:
		print 'URL ' + str(i) + ' not found'

#Tutorial RE - Lena
#http://q3k.org/t4y/Tuts 4 You - Collection 2011/Reversing for Newbies
