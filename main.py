import threading
import requests
import time

class Request(threading.Thread):

    def __init__(self,url):
        super().__init__()
        self.url=url

    def run(self):
        try:
            r=requests.get(self.url)
            if r.status_code<400:
                print("Found subdomains ------->",self.url)
        except:
            pass


user_input=input("Enter your target website:")
st = time.time()
threads=[]
with open("subdomainList.txt","r") as sbl:
    for word in sbl:
        word = word.strip()
        url="http://"+word+"."+ user_input
        t=Request(url)
        t.start()
        threads.append(t)


for t in threads:
    t.join()

print("Search Time:",time.time()-st)