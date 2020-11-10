from bs4 import BeautifulSoup
import subprocess
import requests
from datetime import date
def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return
month = {"January":"1","February":"2","March":"3","April":"4","May":"5","June":"6","July":"7","August":"8","September":"9","October":"10","November":"11","December":"12"}

list = []
req = requests.get('https://www.timeanddate.com/moon/phases/@220244')
soup = BeautifulSoup(req.text, 'html.parser')
for div in soup.find_all('div',{"class":"moon-phases-card"}):
    h3 = div.find('h3')
    links = h3.find('a')
    for link in links:
        if link == "Full Moon":
            FullMoon = div.find('div',{"class":"moon-phases-card__date"}).string
fm = FullMoon
now = date.today()
FullMoon = FullMoon.split()
FullMoon[0] = month[FullMoon[0]]
now = str(now)
now = now.replace('-',' ')
now = now.split()
now.pop(0)
now[0] = int(now[0])
now[1] = int(now[1])
FullMoon[0] = int(FullMoon[0])
FullMoon[1] = int(FullMoon[1])
if FullMoon[0] == now[0] and FullMoon[1] - 2 == now[1]:
    sendmessage("There's a full moon tomorrow")
elif not now[1] == FullMoon[1] + 2 and FullMoon == now or FullMoon[0] == now[0] and FullMoon[1]-1 == now[1] or FullMoon[0] == now[0] and FullMoon[1]+1 == now[1]:
    sendmessage("there's a full moon today")
elif FullMoon[0] == now[0] and FullMoon[1] - 3 == now[1]:
    sendmessage("There's a full moon in two days")
elif FullMoon[0] == now[0] and FullMoon[1] - 4 == now[1]:
    sendmessage("There's a full moon in three days")
else:
    sendmessage(f"the next full moon isn't until {fm}")
