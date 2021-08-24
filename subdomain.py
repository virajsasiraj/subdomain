
# Python script to extract all the subdomains identified from a webpage / URL
# Using Subbrute
# Coded by Viraj Sasiraj @virajsasiraj


import subbrute
from urllib.parse import urlparse
#This module defines a standard interface to break Uniform Resource Locator (URL)

address = input ("enter the url (example: https://example.com):  ")
url= urlparse(address)
domain = url.netloc  # extract the network location


for d in subbrute.run(domain):  # identify subdomains using subbrute
	print (d)
