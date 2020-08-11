from django.shortcuts import render
from django.http import HttpResponse as hr

# Create your views here.
import requests
from bs4 import BeautifulSoup




url = "https://www.flipkart.com/search?q=Realme%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
res = requests.get(url).content

soup = BeautifulSoup(res,"html5lib")

title = soup.find_all('div', class_="_3wU53n")

price = soup.find_all('div', class_="_1vC4OE _2rQ-NK")

rating = soup.find_all('div', class_="hGSR34")


# for t,p,r in zip(title,price,rating):
#
# 	print(t.text)
# 	print(p.text)
# 	print(r.text)

# for i in title:
# 	print(i.text)
#
# for j in price:
# 	print(j.text)
#
# for k in rating:
# 	print(k.text)





def mysite(request):

    # url = "https://www.flipkart.com/search?q=Realme%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    # url3="https://www.flipkart.com/search?q=redmi+8&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=redmi+8%7CMobiles&requestId=88a0e95f-f198-476b-82dd-65026a8d1781&as-backfill=on"
    # ur2='https://www.flipkart.com/search?q=face%20mask&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    #
    # if request.method == :



    if request.POST.get('search'):


        url = request.POST.get('search')
        url=f"https://www.flipkart.com/search?q={url}%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

        res = requests.get(url).content

        soup = BeautifulSoup(res,"html5lib")

        title = soup.find_all('div', class_="_3wU53n")

        price = soup.find_all('div', class_="_1vC4OE _2rQ-NK")

        rating = soup.find_all('div', class_="hGSR34")

        titles=[]
        prices=[]
        ratings=[]
        ooo=0
        kkk=0
        yyy=0
        for j in price:

            print(j.text)
            prices+=j
            ooo+=1

        # for j in price:
        #     print(j.text)
        #     prices+=j


        for i in range(ooo) :

            #print(k.text)
            #ratings+=''.join(k.stripped_strings)
            #ratings+=k.text.stripped_strings
            #ratings+=k.text
            # ratings+=str(k)
            # print(str(k))
            # print(type(k))
            h=soup.find_all('div', class_="_3wU53n")[yyy].text
            print(h)
            titles+=h,
            yyy+=1

        # for k in rating:
        #     print(k.text)
        #     ratings+=k.text,

        # for k in rating:
        #     print(k.text)
        #     #ratings+=''.join(k.stripped_strings)
        #     #k.replace(',','')
        #     ratings+=k

        # for k in rating:
        #     print(k.text)
        #     ratings+=k.text,
        #     #k.replace(',','')
        #     #ratings+=k
        'mainnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
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






        kk='''
        {% for i in {titles} %}
        {i}
        {% endfor %}



        '''
        k=[titles,prices,ratings]
        print(ratings)
        print(ooo)
        print(yyy)
        print(kkk)

        return render(request,'hello/mysite.html',{'titles':titles,'prices':prices,'ratings':ratings,'k':k})

    return render(request,'hello/mysite.html')




















'''
{% for i in titles %}
{{i}}
<br />
{% endfor%}
{% for i in prices %}
{{i}}
<br />
{% endfor%}
{% for i in ratings %}
{{i}}
<br />
{% endfor%}
'''
