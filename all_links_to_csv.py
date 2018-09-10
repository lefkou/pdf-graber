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
	page = urlopen(req)
	soup = BeautifulSoup(page, features="lxml")
	# print([a.get('href') for a in soup.find_all('a', href=True)])
	# all links in each page related to the pdfs
	links = []
	for link in soup.find_all('a'):
		href = link.get('href')
		# print("hiii+++:" + href)
		if contains in href:
			links.append(prefix + href)
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


# print(">>>>>>>>>>>>Newwwwww pdf!!!!!!!!!!!!")

# print(get_links(hrefs[0]))
# print(len(hrefs))
# for h in hrefs:
# 	print(h)
# print(hrefs)
myFile = open('links.csv', 'w')
with myFile:
    writer = csv.writer(myFile, dialect='excel')
    writer.writerows(np.transpose([hrefs]))
     
print("Writing complete")
# print()
# print(get_links(hrefs[0], prefix="", contains="pdf"))

# for link in BeautifulSoup(response.content, "html.parser", parse_only=SoupStrainer('a', href=True)):
#     print(link['href'])
# r = requests.get(hrefs[0], allow_redirects=True)
# print(r)
# filename = get_filename_from_cd(r.headers.get('content-disposition'))
# print(filename)
# open(filename, 'wb').write(r.content)


# headers = {'User-Agent':'Mozilla/5.0'}
# req = Request(hrefs[0], headers=headers)
# page = urlopen(req)
# soup = BeautifulSoup(page, 'html.parser')

# for link in soup.findAll('a'):
#     print(link.get('href'))
