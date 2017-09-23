import requests
from bs4 import BeautifulSoup
import operator
url="https://seattle.craigslist.org/search/jjj"

def start(url):
    word_list=[] #this is a blank list
    source_code=requests.get(url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,"html.parser")

    for posts_text in soup.find_all('a',{'class': 'result-title hdrlnk'}):
        content=posts_text.string
        words= content.lower().split() #content is sentence...lower() is used to lower case.. split() is used for splliting sentence in to words
        for each_word in words:
            word_list.append(each_word)#add words into the list

    clean_up_list(word_list) #for cleaning unncessary characters

#cleaning uncessary characters
def clean_up_list(word_list):
    symbols = "!@#$%^&*()-+={}\"[];:'|<,.>/?"
    clean_word_list=[]
    for word in word_list:
        for i in range(0,len(symbols)):
            word=word.replace(symbols[i], "")#replace symbol with nothing
        if len(word)>0:
            #print(word)
            clean_word_list.append(word)
           # print(len(clean_word_list))
    create_dictionary(clean_word_list)


def create_dictionary (clean_word_list):
    word_count={}
    for word in clean_word_list:
        if word in word_count:
            word_count[word]+=1 #this increases value of the word in dictionary ..look dictionary.py for understanding
        else:
            word_count[word]=1

    for key,value in sorted(word_count.items(), key=operator.itemgetter(1)): #the parameter key is different to variabble key in for loop
        pass
        print(key,value)

start(url)