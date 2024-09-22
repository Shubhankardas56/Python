from bs4 import BeautifulSoup
import urllib.request
scorepage='https://www.cricbuzz.com/live-cricket-scores/35632/7th-match-indian-premier-league-2021.xml'
page=urllib.request.urlopen(scorepage)
soup=BeautifulSoup(page,'html.perser')
result=soup.find_all('description')
ls=[]
for match in result:
    ls.append(match.get_text())
print(ls)