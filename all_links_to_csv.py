from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib3
import requests
import re
import csv
import numpy as np 

# returns an array of link from a page
def get_links(url, prefix="", contains=""):
	headers = {'User-Agent':'Mozilla/5.0'}
	req = Request(url,headers=headers)
	try:
		page = urlopen(req)
		soup = BeautifulSoup(page, features="html5lib")
		# print([a.get('href') for a in soup.find_all('a', href=True)])
		# all links in each page related to the pdfs
		links = []
		for link in soup.find_all('a'):
			href = link.get('href')
			# print("hiii+++:" + href)
			if contains in href:
				links.append(prefix + href)
	except:
		return ['Not available!']
	return links


# create urls for all 7 pages
urls = []
for i in range(1,8): 
	urls.append('https://ww2.eagle.org/content/eagle/en/rules-and-resources/rules-and-guides/jcr:content/par/rulesandguides.ajax.html?t=publication&sc=true&p=/content/dam/eagle/rules-and-guides/current&q=&f=all&s=pubnum&o=keep&sp=&pn={}'.format(i))


# get all the links from the 7 urls constructed above
all_links = []
for url in urls:
	all_links.append(get_links(url, prefix="https://ww2.eagle.org/en/rules-and-resources/rules-and-guides.html", contains='content/dam/eagle/rules-and-guides/current/'))

hrefs = []
for page in all_links:
	for link in page:
		hrefs.append(link)

download_prefix = "https://ww2.eagle.org/content/eagle/en/rules-and-resources/rules-and-guides/jcr:content/par/rulesandguides.ajax.html?t=documents&sc=true&p=/content/dam/eagle/rules-and-guides/current&sp="


pages_with_links = []
# print(len(hrefs))
for row in hrefs:
	# print(row.split("html#")[1])
	pages_with_links.append(download_prefix+row.split("html#")[1])

pdf_links_lst = []
for i in range(len(pages_with_links)):
	pdf_links_lst.append(get_links(pages_with_links[i], prefix='https://ww2.eagle.org/', contains='.pdf'))


pdf_links = []
for page_lst in pdf_links_lst:
	for page in page_lst:
		if 'Not available!' not in page:
			pdf_links.append(page)

myFile = open('pdf_links.csv', 'w')
with myFile:
    writer = csv.writer(myFile, dialect='excel')
    writer.writerows(np.transpose([pdf_links]))
     
print("Writing complete")