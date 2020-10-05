#짜투리 기능? 먼저 따로 만들어 놓기. 메타태그 크롤링하는 코드

from pymongo import MongoClient #pymongo 쓸게
client = MongoClient('localhost', 27017) #내 컴터에서 돌고 있는 파이몽고에 접
db = client.dbsparta #dbsparta라는 이름의 db에 접근하라. 없으면 만들어

import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
#print(soup)
title = soup.select_one('meta[property="og:title"]')['content']
image = soup.select_one('meta[property="og:image"]')['content']
desc = soup.select_one('meta[property="og:description"]')['content']
print(title, image, desc)