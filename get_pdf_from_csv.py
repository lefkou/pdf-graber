import requests
import shutil
import urllib.request

# go through the pdf link dataset and donwload all links
with open("pdf_links.csv") as f:
    for url in f:
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        # format name of pdf files
        urllib.request.urlretrieve(url, str(url).rsplit('/', 1)[1].split('.')[0]+'.pdf')
