import pandas as pd


# open dataset
df = pd.read_csv('./pdf_links.csv', header=None)
df.index += 1
# add column name
df = df.rename(columns={ df.columns[0]: "file_url" })
# add 1 extra column with download status
df['downloaded'] = False
# drop duplicates
df = df.drop_duplicates(subset='file_url', keep='first')
# save file and remove index
df.to_csv('pdf_links_final.csv', index=False)