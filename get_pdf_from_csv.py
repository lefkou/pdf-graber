import requests
import shutil
import urllib.request
import pandas as pd


# go through the pdf link dataset and donwload all links


df = pd.read_csv('./pdf_links_final.csv')
df.index += 1
# print(df)

for index, row in df.iterrows():
    # print(row['file_url'], row['downloaded'])
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    # format name of pdf files
    try:
        filename =  str(row['file_url']).rsplit('/', 1)[1].split('.')[0]+'.pdf'
        urllib.request.urlretrieve(row['file_url'], filename)
        row['downloaded'] = True
    except: 
        row['downloaded'] = False
    