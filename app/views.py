from django.shortcuts import render

from bs4 import BeautifulSoup

import requests

# Create your views here.


def get_html_content(city):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    city = city.replace(' ', '+')

    html_content = session.get(f'https://www.google.com/search?ei=4jMwX4veIs6y9QPRnKC4DQ&q=weather+in+{city}').text

    return html_content


def data(request):

    if 'city' in request.GET:


        #headers = {'Accept-Language' : 'en-US,en;q=0.8' }

        city = request.GET.get('city')


        html_content =  get_html_content(city)

        soup = BeautifulSoup(html_content,'html.parser')

        region = soup.find('div',attrs={'id': 'wob_loc'}).text

        daytime = soup.find('div', attrs ={'id' : 'wob_dts'}).text

        status = soup.find('span', attrs={'id' : 'wob_dc'}).text

        temp = soup.find('span', attrs={'id' : 'wob_tm'}).text


        print(region)






    context = {

        'r' : region,
        'daytime' : daytime,
        'status' : status,
        'temp' : temp,


    }

    return render(request,'app/test.html',context)