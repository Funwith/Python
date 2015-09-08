# Application: pyDownload
# Language: Python 2.7
# Development Environment: Windows 8.1
# Author: Vietworm
# Description: Download document file from URL: http://www.cse.hcmut.edu.vn/~hungnq/courses/ 

# Dependency: requests, scrapy
# Installation: pip install <package>

import os
import requests
import urllib
import scrapy
import mimetypes
URI = 'http://www.cse.hcmut.edu.vn/~hungnq/courses/lopchuyendoi/'
_name = 'pyDownload'

def html(url):
	"""
	A head process URL, return http header information array.
	"""
	r = requests.get(url)
	result = []
	result.extend([r.status_code,r.headers['content-type'],r.text,r.encoding, r.headers['content-length']])
	print result
	return result

# Check Content Type from URL
# isFile return contains 'application', isDirectory return contains 'text/html'	

# Get file type using mimetypes modules
def isFile(url):
	"""
	Return boolean True or False, using check file type of URL.
	"""
	if mimetypes.guess_type(url, strict=True)[0] == None:
		return False
	else:
		return True
	
def scrapyExtract(url):
	"""
	Scrapy modules, get attributes html text plain for after process. 
	"""
	r = html(url) # Return array from requests [status_code, content-type, text/plain, encoding]
	sel = scrapy.Selector(text=r[2], type="html")
	return sel.xpath('//td//@href').extract()[1:] # Find @href value from text/plain.

def download(path, fileName):
	"""
	Download file from URL.
	"""
	fileSave = os.path.join(_name, fileName)
	d = urllib.URLopener()
	d.retrieve(path, fileSave)
	
def chalk(string, status, bold):
	"""Supported for highlight print messages to commandline (on windows) or terminal (on Unix).
	Example: print chalk('pyDownload', 'green', False)"""
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
	"""
	Created folder 'pyDownload for save as to folder' and process download file.
	"""
	if os.path.exists(_name) == False:
		os.mkdir(_name)
		print "\nThe directory was created successfully."
		
	for i in location:
		url = URI + i
		if isFile(url):
			try:
				download(url, i)
				print '\nSuccessfully: ' + url
			except IOError:
				print "\n### URL: " + url + " can't download."
		else:
			subLocation = scrapyExtract(url)
			if not subLocation:
				print '\n### Directory is empty.'
				break
			main(subLocation, URI + i)	

if __name__ == "__main__":
	location = scrapyExtract(URI)
	print '\nURI: found ' + str(len(location)) + ' items.'
	main(location, URI)
