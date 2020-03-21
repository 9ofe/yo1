import os
import random
import string
import threading
import time
from queue import Queue
import platform

import requests
from colorama import Fore, init

intro = """
View Bots c,c
"""

print(intro)

if platform.system() == "Windows": #checking OS
    clear = "cls"
else:
    clear = "clear"

token = input("ID?\n")
url= "https://m.youtube.com/watch?v=" + token
url2 = "https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=Syr16u8qwHnPkVqI&docid=" + token + "&ver=2&cmt=2094&ei=1EJtXou2C6eoxN8PpqqNqAg&fmt=133&fs=0&rt=1769&of=rkW8h_g-Pta1U6EIuWGdvw&euri&lact=7275&live=dvr&cl=300532980&state=playing&vm=CAEQABgEKhhJc0gwZ2w0QmFfbTBWSXlWNm9ITmRRPT06MkFOcHN5N0FhUWlHOHl5QkQySUF1OGt6amlZYjZwN3hzNzRXV3hhTEE4NDZVU1h2TTV3&volume=100&c=MWEB&cver=2.20200313.03.00&cplayer=UNIPLAYER&cbrand=apple&cbr=Safari%20Mobile&cbrver=12.1.15E148&cmodel=iphone&cos=iPhone&cosver=12_2&cplatform=MOBILE&delay=5&hl=ru&cr=IQ&rtn=2069&afmt=140&lio=1556394045.182&idpj=&ldpj=&rti=1769&muted=0&st=2094&et=2394"
class main(object):
    def __init__(self):
        self.combolist = Queue()
        self.Writeing = Queue()
        self.printing = []
        self.botted = 0
        self.combolen = self.combolist.qsize()

    def printservice(self): #print screen
        while True:
            if True:
                os.system(clear)
                print(Fore.LIGHTCYAN_EX + intro + Fore.LIGHTMAGENTA_EX)
                print(
                    Fore.LIGHTCYAN_EX + f"Botted:{self.botted}\n")
                for i in range(len(self.printing) - 10, len(self.printing)):
                    try:
                        print(self.printing[i])
                    except (ValueError, Exception):
                        pass
                time.sleep(0.5)
a = main()
class proxy():

    def update(self):
        while True:
            url = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&ssl=yes"
            r = requests.get(url)
            self.splited = r.text.split("\r\n") #scraping and splitting proxies
            time.sleep(600)
    
    def get_proxy(self):
        random1 = random.choice(self.splited) #choose a random proxie
        return random1
    def FormatProxy(self):
	    proxyOutput = {'https':self.get_proxy()}
	    return proxyOutput

    def __init__(self):
        self.splited = []
        threading.Thread(target=self.update).start()
        time.sleep(3)

proxy1 = proxy()
def bot():
    while True:

        


        headers={
        "Host": "m.youtube.com",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "close"
        }

        try:
            s = requests.session()
            s.get(url,headers=headers,proxies=proxy1.FormatProxy()) #stream request
            s.get(url2,headers=headers,proxies=proxy1.FormatProxy()) #api request

            a.botted += 1
        except:
            pass



maxthreads = int(input("How many Threads? Recommended: 500 - 1000\n"))

threading.Thread(target=a.printservice).start()
num = 0
while num < maxthreads :
    num += 1
    threading.Thread(target=bot).start()


threading.Thread(target=bot).start()
