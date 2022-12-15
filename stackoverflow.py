import requests
import json
from bs4 import BeautifulSoup
res=requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# soup=BeautifulSoup(res.text,'html.parser')

# question=soup.find_all(class_="s-post-summary js-post-summary")
# # div=soup.find("div",{"id":"question-summary-73139272"})
# ans=soup.find_all(class_="s-link")
for ques in res.json()['items']:
    if ques['is_answered']:
        print(ques['title'])
