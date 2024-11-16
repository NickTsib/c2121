from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "sc-b3fc6b7-0"}) #<div class="sc-b3fc6b7-0 dzgUIj fall"><span>$91,096.78</span></div>
    res = soup_list[0].find("span")
    res1 = soup_list[1].find("span")
    print(str(res)[6:-7])
    print(str(res1)[6:-7])
    for i in soup_list:
        print(i)


