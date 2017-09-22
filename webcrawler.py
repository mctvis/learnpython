
import requests
from bs4 import BeautifulSoup
'''
#create a core spider in trading section of website
def trade_spider(max_pages):
    page=1
    while page<=max_pages:
        url="https://thenewboston.com/search.php?type=1&sort=pop&page=" + str(page)
        source_code = requests.get(url)
        plain_text=source_code.text #the website is stored as plain text
        soup = BeautifulSoup(plain_text, "html.parser") #creating a object soup of class 'BeautifulSoup' Note the use of constructor for intializing the obeject ..def _init_
        for link in soup.find_all('a', {'class': 'item-name'}): #getting all links of the title where link= <a href="page.php?pid=344" class="user-name">Java</a>
            href = link.get('href')
            print(href)
        page+=1

trade_spider(1)
'''
def craig_spider(max_pages):
    page = 120
    while page <= max_pages:
        url = "https://cnj.craigslist.org/search/sya?s=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.find_all("a", {"class": "result-title hdrlnk"}):
            href =link.get("href")#get the href in <a href="">
            title = link.string#the actual string in link eg<title>"Welcome"</title
            #print(title)
            #print(href)#can also do print(title,href)
            get_single_item_data(href) #loop inside loop
        page += 120


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.find_all("span", {"id": "titletextonly"}):
        print(item_name.string)
    for link in soup.find_all("a"):
        href=link.get("href")
        #print(href)

craig_spider(240)





