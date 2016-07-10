__author__ = "VIshu"

import requests
from bs4 import BeautifulSoup

requests = requests.get("http://us.johnlewis.com/store/john-lewis-wade-office-chair-black/p447855")
content = requests.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
price = float(element.text.strip().replace("$",""))
print price
