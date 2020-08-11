import requests
from bs4 import BeautifulSoup


url = "https://www.flipkart.com/search?q=Realme%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
res = requests.get(url).content

soup = BeautifulSoup(res,"html5lib")

title = soup.find_all('div', class_="_3wU53n")

price = soup.find_all('div', class_="_1vC4OE _2rQ-NK")

rating = soup.find('div', class_="hGSR34").text



titles=[]
prices=[]
# ratings=''
ratings=[]
for i in title:
    #print(i.text)
    titles+=i
ooo=0
for j in price:
    #print(j.text)
    prices+=j
    ooo+=1
print(ooo)
kkk=0
for i in range(ooo) :

    #print(k.text)
    #ratings+=''.join(k.stripped_strings)
    #ratings+=k.text.stripped_strings
    #ratings+=k.text
    # ratings+=str(k)
    # print(str(k))
    # print(type(k))
    h=soup.find_all('div', class_="hGSR34")[kkk].text
    print(h)
    ratings+=h,
    kkk+=1

#k=[titles,prices,ratings]

print(ratings)
print(titles)
print(prices)
print(h)
