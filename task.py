import requests, sys, re
from bs4 import BeautifulSoup

name = list(sys.argv[1])

result = 0
for i in range(len(name)):
    response = requests.get('http://www.kanjipedia.jp/search?k=' + name[i] + '&kt=1&sk=leftHand')

    soup = BeautifulSoup(response.text, 'html.parser')
    url = 'http://www.kanjipedia.jp' + soup.find(id='resultKanjiList').a.get('href')

    url_response = requests.get(url)
    url_soup = BeautifulSoup(url_response.text, 'html.parser')

    strokes = int(re.sub(r'\D', '', url_soup.find(class_='kanjiKakusu').text))

    print(name[i] + '   ' + str(strokes) + '画')
    result += strokes

print('合計 ' + str(result) + '画')
