from bs4 import BeautifulSoup
import requests 


r = requests.get( 'https://example.com/')
soup = BeautifulSoup(r.text, 'html.parser')

print(soup.find_all("p"))