# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
from urllib import request

baseUrl = 'https://movie.douban.com/top250?start=25%dfilter='


def get_item(start):
    url = baseUrl % start
    movies = []
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    items = soup.find('ol', 'grid_view').find_all('li')
    for i in items:
        movie = {}
        movie['poster'] = i.find('div', 'item').find('div', 'pic').find('img').get('src')
        movies.append(movie)
    return movies


if __name__ == "__main__":
    start = 0
    temp = 1
    while (start < 250):
        movies = get_item(start)
        for i in movies:
            print(i['poster'])
            # temp = i[ 'poster' ].split("/")[-1]
            request.urlretrieve(i['poster'], '%d.jpg' % temp)
            temp += 1
        start += 25
