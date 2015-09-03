# Language: Python
# Development Environment: Windows 8.1
# Author: Vietworm
# Description: Download document file from URL: http://www.cse.hcmut.edu.vn/~hungnq/courses/ 

# Dependency: requests, scrapy, urllib
# Installation: pip install <package>

import requests
import urllib
import scrapy
import mimetypes
URI = 'http://www.cse.hcmut.edu.vn/~hungnq/courses/'

def html(url):
	r = requests.get(url)
	result = []
	result.extend([r.status_code,r.headers['content-type'],r.text,r.encoding, r.headers['content-length']])
	return result

def getFileInfo(url):
	r = urllib.urlopen(url)
	http_message = r.info()
	type = http_message.type
	return type
	
# Check Content Type from URL
# isFile return contains 'application', isDirectory return contains 'text/html'	

# Get file type using mimetypes modules
def isFile(url):
	if mimetypes.guess_type(url, strict=True)[0] == None:
		return False
	else:
		return True
		
# Check has content from new URL		
def hasContent(url):
	return
	
def scrapyExtract(url):
	r = html(url) # Return array from requests [status_code, content-type, text/plain, encoding]
	sel = scrapy.Selector(text=r[2], type="html")
	return sel.xpath('//td//@href').extract()[1:] # Find @href value from text/plain.

def download(path, fileName):
	d = urllib.URLopener()
	d.retrieve(path, fileName)
	
def hilite(string, status, bold):
    attr = []
    if status:
        # green
        attr.append('32')
    else:
        # red
        attr.append('31')
    if bold:
        attr.append('1')
    return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)	
	
def main(location, URI):
	for i in location:
		print 'Download: ' + i
		url = URI + i
		if isFile(url):
			try:
				download(url, i)
				print 'Successfully: ' + url
			except IOError:
				print "####URL: " + url + " can't download"
		else:
			subLocation = scrapyExtract(url)
			if not subLocation:
				print 'Directory is Empty'
				break
			main(subLocation, URI + i)	
	
# print hilite('crawler','green',False)	

# Recursive funtion load directory and download file.
location = scrapyExtract(URI)
print 'URI: found ' + str(len(location)) + ' items\n'
main(location, URI)
