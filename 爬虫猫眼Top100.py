import requests
from requests.exceptions import RequestException
import re
import json
from  multiprocessing import Pool

def get_one_page(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    patter = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                        +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                        +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(patter,html)
    for i in items:
        yield {
            'index': i[0],
            'image': i[1],
            'title': i[2],
            'actor': i[3].strip()[3:],
            'time':  i[4].strip()[5:],
            'score': i[5]+i[6]
        }
def  write_to_file (content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=0)+'\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for i in parse_one_page(html):
        print(i)
        write_to_file(i)
if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(main,[a*10 for a in range(10)])



