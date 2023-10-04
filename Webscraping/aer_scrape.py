#This was created by Radekz, being used for references.
import requests
import pandas as pd
from bs4 import BeautifulSoup

data = []
data2 = []

#20190415
# 20185000, 20190000 says empty
# 20175000, 20180000 says empty
# 20165000, 20170000 says empty

for i in range(20155000, 20160000):
    url = 'https://www.aeaweb.org/articles?id=10.1257/aer.' + str(i)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    keywords = soup.find("meta", attrs={'name': 'keywords'})
    if keywords is None:
        continue

    keywords = keywords.get("content")
    title = soup.find("meta", attrs={'name': 'citation_title'}).get("content")
    authors = [meta.get("content") for meta in soup.find_all("meta", attrs={'name': 'citation_author'})]
    institutions = [meta.get("content") for meta in soup.find_all("meta", attrs={'name': 'citation_author_institution'})]
    pubdate = soup.find("meta", attrs={'name': 'citation_publication_date'}).get("content")
    journal = soup.find("meta", attrs={'name': 'citation_journal_title'}).get("content")
    issn = soup.find("meta", attrs={'name': 'citation_issn'}).get("content")
    vol = soup.find("meta", attrs={'name': 'citation_volume'}).get("content")
    issue = soup.find("meta", attrs={'name': 'citation_issue'}).get("content")
    fpage = soup.find("meta", attrs={'name': 'citation_firstpage'}).get("content")
    lpage = soup.find("meta", attrs={'name': 'citation_lastpage'}).get("content")
    description = soup.find("meta", attrs={'name': 'twitter:description'}).get("content")

    # Extracting JEL codes
    jel_codes_elements = soup.find_all('strong', class_='code')
    jel_codes = [code_elem.text for code_elem in jel_codes_elements]

    data.append({
        'url': url,
        'keywords': keywords,
        'title': title,
        'authors': authors,
        'institutions': institutions,
        'pubdate': pubdate,
        'journal': journal,
        'issn': issn,
        'vol': vol,
        'issue': issue,
        'fpage': fpage,
        'lpage': lpage,
        'description': description,
        'jel_codes': jel_codes
    })


#print(data1)
print(data)

# Create a pandas DataFrame from the collected data
df = pd.DataFrame(data)
#df2 = pd.DataFrame(data2)

#df[["day", "month", "year"]] = df["institutions"].str.split(",", expand = True)
#pd.concat([df[[0]], df['institutions'].str.split(',', expand=True)], axis=1)
# Printing the DataFrame
print(df)

z=df.to_csv()

print(z)

