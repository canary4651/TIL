import os
from time import sleep
import pandas as pd

BASE_URL = 'https://place.map.kakao.com/main/v/'

ids = pd.read_csv('cafe1.csv')['0'].values
ids = list(ids)
ids = ids[ids.index(727257029):2048]

os.system('mkdir -p data')

def check_file(filename):
    with open(filename) as f:
        text = f.read()
        if text[:1] != '{':
            print('에러!')
            os.exit()

for i, id in enumerate(ids):
    print(i + 1, id)
    os.system(f'curl {BASE_URL}{id} > data/{id}.json')
    check_file(f'data/{id}.json')
    sleep(5)
    print('-' * 80)

print('complete!')

# 에러!
# Traceback (most recent call last):
#   File "download.py", line 23, in <module>
#     check_file(f'data/{id}.json')
#   File "download.py", line 18, in check_file
#     os.exit()
# AttributeError: module 'os' has no attribute 'exit'