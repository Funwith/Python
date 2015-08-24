import urllib
import requests
download = urllib.URLopener()
for i in range(10,41):
	url = 'http://q3k.org/t4y/Tuts 4 You - Collection 2011/Reversing for Newbies/snd-reversingwithlena-tutorial' + str(i) + '.tutorial.rar'
	download.retrieve(url,str(i) + '.rar')
	print 'Download ' + url 

