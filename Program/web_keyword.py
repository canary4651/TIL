import hashlib
import time
from collections import deque

from bs4 import BeautifulSoup
import requests
from newspaper import Article

​# 키워드로 크롤링하기 
visited = {}
queue = deque()
​
def fetch(url):
    return requests.get(url)​

def get_links(soup):
    return soup.find_all('a')
​
​
def get_filename(url):
    return hashlib.sha1(url.encode('utf-8')).hexdigest() + '.html'
​
​
def has_keywords(html, keywords): #html, keywords로 받기 
    article = Article('')
    article.set_html(html)
    for keyword in keywords:
        if keyword in article.title or keyword in article.text: #타이틀이나, 기사에 존재하면 반환하기 
            return True
    return False
​
​
def crawl(url, keywords):
    print(f'Fetching {url}')
    resp = fetch(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = get_links(soup)
​
        # 내용을 파일로 저장하거나, 뭔가 다른 일을 하기
        if has_keywords(resp.text, keywords):
            with open(get_filename(url), 'wb') as fout:
                fout.write(resp.text.encode('euc-kr'))
​
        for link in links:
            href = link.get('href')
            if href.startswith('https://news.naver.com/main/read.nhn') and href not in visited:
                queue.append(href)
                visited[href] = 0
    else:
        print(f'Failed to fetch {url}')
​
​
if __name__ == '__main__':
    queue.append('https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=009&aid=0004445715')
​
    while queue:
        url = queue.popleft()
        crawl(url, ['김정은', '북한'])
        time.sleep(1)