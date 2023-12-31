import threading
import queue

import requests

q = queue.Queue()
valid_proxies = []

with open("proxy-list3.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)
    
def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get('https://ipinfo.io/json', 
            proxies={'http': proxy,
                     'https': proxy})
            if res.status_code == 200:
                print(proxy)
        except:
            continue
   

for t in range(10):
    threading.Thread(target=check_proxies).start()