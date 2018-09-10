from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# returns an array of link from a page
def get_links(url):
	headers = {'User-Agent':'Mozilla/5.0'}
	req = Request(url,headers=headers)
	page = urlopen(req)
	soup = BeautifulSoup(page, features="lxml")
	# print([a.get('href') for a in soup.find_all('a', href=True)])
	prefix = "https://ww2.eagle.org/en/rules-and-resources/rules-and-guides.html"

	# all links in each page related to the pdfs
	links = []
	for link in soup.find_all('a'):
		href = link.get('href')
		if 'content/dam/eagle/rules-and-guides/current/' in href:
			links.append(prefix + href)
	return links


urls = []
for i in range(1,8): 
	urls.append('https://ww2.eagle.org/content/eagle/en/rules-and-resources/rules-and-guides/jcr:content/par/rulesandguides.ajax.html?t=publication&sc=true&p=/content/dam/eagle/rules-and-guides/current&q=&f=all&s=pubnum&o=keep&sp=&pn={}'.format(i))

all_links = []
for url in urls:
	all_links.append(get_links(url))



for page in all_links:
	for link in page:
		print(link)


