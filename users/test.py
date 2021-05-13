from bs4 import BeautifulSoup
import requests



url = "https://www.moneycontrol.com/markets/indian-indices/"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

sensex = soup.find("span", id="indcur").get_text()
print(sensex)


url = "https://www.moneycontrol.com/markets/indian-indices/top-nse-50-companies-list/9?classic=true"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')
nifty = soup.find('span', id='indcur').get_text()
print(nifty)

