from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "sc-142c02c-0"})
    res = soup_list[0].find("span")
    print(res.text)