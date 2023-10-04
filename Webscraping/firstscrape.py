
import requests, bs4

# download the main page from Project Gutenberg
res = requests.get('https://gutenberg.org')
res.raise_for_status()   # check request status
res       # prints status
res.text   # prints downloaded text

# Pass the text attribute of the response to bs4.BeautifulSoup
gutenbergSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(gutenbergSoup))
gutenbergSoup   # parsed HTML code

