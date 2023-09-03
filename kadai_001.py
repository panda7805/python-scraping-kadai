import requests
from bs4 import BeautifulSoup
url = 'https://news.yahoo.co.jp/articles/51e132245dbd0306ec8d86ed104ce97ad2fe6468'

# GETリクエストを送信し、HTMLを取得する
response = requests.get(url)

# HTMLを解析する
soup = BeautifulSoup(response.text, 'html.parser')

# 本文の要素を取得する
# CSSセレクタを使用して、本文を取得する
content_element= soup.select_one('#uamods>.article_body>div>p')

# 本文のテキストを取得する
content_text = content_element.text

print(content_text)
