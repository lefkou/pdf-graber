import requests
import shutil
import urllib.request


with open("pdf_links.csv") as f:
    for url in f:
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, str(url).rsplit('/', 1)[1].split('.')[0]+'.pdf')
        