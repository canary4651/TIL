from collections import deque
import csv
from datetime import datetime
import hashlib
import random
import sys
import time
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from logbook import Logger, StreamHandler
import requests

StreamHandler(sys.stdout).push_application()
log = Logger(__name__)

# 상수로 .csv 파일의 경로를 설정했지만, 명령창 인자로 받을 수 있도록 만들면
# 조금 더 유연한 프로그램이 될 것 같습니다.
#
# 과제: 크롤링한 페이지 정보를 저장할 .csv 파일 이름을 명령창 인자로 받을 수
# 있도록 변경하기.
CSV_PATH = 'pages.csv'

# 최초의 계획은 dict를 이용해서 URL과 함께 해당 주소를 방문한 날짜를 기록해
# 두었다가 추가적인 작업 (예를 들면, 너무 오래된 방문일 경우 재방문 하기)을
# 하려는 계획이 있었지만, 코드가 복잡해질 것 같아서 URL만 저장하도록
# 변경하였습니다.
#
# 과제: 이렇게 하면 프로그램을 종료할 경우 기존에 방문했던 모든 기록이
# 사라집니다. visited와 queue의 내용을 파일에 저장해 두었다가 프로그램을
# 종료했다가 다시 실행시켰을 때 기존의 내용을 다시 불러올 수 있도록 변경하기.
visited = set()
queue = deque()


def find_links(soup, url):
    """BeautifulSoup 문서에서 <a> 태그를 모두 가져와서 href가 같은 도메인
    이름에서 파생된 경우에만 리턴하도록 합니다.
    """
    parsed_url = urlparse(url)
    prefix = f'{parsed_url.scheme}://{parsed_url.netloc}'
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith(prefix):
            yield href


def process_content(soup, encoding, url, fetched_at):
    # 웹페이지의 내용을 별도의 파일에 저장합니다.
    filename = get_filename(url)
    with open(filename, 'w') as fout:
        fout.write(soup.text)

    # NOTE: .csv 파일 핸들을 열어놓고 계속 사용하는 편이 훨씬 효율적이긴 하지만
    # 그렇게 할 경우 프로그램 구조가 지금보다 아주 조금(?) 복잡해지기 때문에
    # 이해하기 쉬운 코드 구조를 유지하기 위해 조금 비효율적인 방법으로 .csv
    # 파일을 다룹니다.
    with open(CSV_PATH, 'a') as fout:
        writer = csv.writer(fout)
        formatted_dt = fetched_at.strftime('%Y-%m-%d %H:%M:%S')
        title = soup.title.text.strip()
        writer.writerow([formatted_dt, title, url, filename])


def get_filename(url):
    """URL을 그대로 파일 이름으로 사용하기 어렵기 때문에 SHA1 해시 함수를
    이용해서 파일 이름을 도출합니다.
    """
    return hashlib.sha1(url.encode('utf-8')).hexdigest() + '.html'


def crawl(url):
    log.info(f'Fetching {url}')

    resp = requests.get(url)
    fetched_at = datetime.now()

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = find_links(soup, url)
        process_content(soup, resp.encoding, url, fetched_at)

        for link in links:
            # 어떤 경우에는 충분히 robust하지 못한 모습을 보여줍니다. 예를
            # 들어서, 다음의 두 URL을 다른 URL로 인식하기 때문에 같은
            # 페이지임에도 불구하고 두 번 방문하게 됩니다.
            #
            # https://finance.yahoo.com
            # https://finance.yahoo.com/
            #
            # 또한, 다음과 같이 의미상 같은 URL이지만, 변수의 순서가 바뀌었기
            # 때문에 다른 URL로 인식되는 문제도 가지고 있습니다.
            #
            # https://google.com/search?q=test&hl=en-us
            # https://google.com/search?hl=en-us&q=test
            #
            # 과제: 이러한 경우 같은 URL이라는 것을 인식할 수 있도록 코드를
            # 수정하기.
            if link not in visited:
                queue.append(link)
                visited.add(link)
    else:
        log.warn(f'Failed to fetch {url}')


if __name__ == '__main__':
    # 명령창 인자로 URL을 받습니다. 코드를 단순하게 유지하기 위해 sys.argv 를
    # 직접 참조했지만, 실제 프로그램을 작성할 때에는
    # Click (https://click.palletsprojects.com) 같은 라이브러리를 사용하는
    # 것을 추천합니다.
    init_url = sys.argv[1]
    queue.append(init_url)

    while queue:
        url = queue.popleft()
        crawl(url)

        # 랜덤으로 0-2초간 휴식을 취합니다. 단시간에 너무 많은 요청을 보내면
        # 스팸봇으로 인식될 가능성이 있습니다.
        time.sleep(random.random() * 2)