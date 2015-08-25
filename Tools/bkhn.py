# Language: Python
# Development Environment: Windows 8.1
# Author: 0xgi
# Description: Download document file from URL: http://www.cse.hcmut.edu.vn/~hungnq/courses/ 

# Dependency: requests, scrapy, urllib
# Installation: pip install <package>

import requests
import urllib
import scrapy
URI = 'http://www.cse.hcmut.edu.vn/~hungnq/courses/501120/'

def html(url):
	r = requests.get(url)
	result = []
	result.extend([r.status_code,r.headers['content-type'],r.text,r.encoding])
	return result

# Check Content Type from URL
# isFile return contains 'application', isDirectory return contains 'text/html'	

# FIXME: Using content-type for check file type is bad idea.
# Request as well as file download :( Long time request for check file type.
def isFile(contentType):
	if not "text/html" in contentType:
		return True
	else:
		return False

# Check has content from new URL		
def hasContent(url):
	return
	
def scrapyExtract(url):
	r = html(url) # Return array from requests [status_code, content-type, text/plain, encoding]
	sel = scrapy.Selector(text=r[2], type="html")
	return sel.xpath('//td//@href').extract()[1:] # Find @href value from text/plain.

def download(path):
	d = urllib.URLopener()
	d.retrieve(path)
	
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
	
# print hilite('crawler','green',False)	

# Recursive funtion load directory and download file.
location = scrapyExtract(URI)
print 'URI: found ' + str(len(location)) + ' items'
for i in location:
	result = html(URI + i)
	if result[0] == 200 and isFile(result[1]) == False:
		print 'Directory'
	else:
		print 'File'