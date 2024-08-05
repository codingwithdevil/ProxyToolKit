import requests as rqs
from bs4 import BeautifulSoup
from .Exceptions import *
import random
from pyProxy.agents import user_agents

class scrapeProxy():
    def __init__(self):
        self.proxy_types = ['all','http','https','socks4','socks5']
        self.proxyscrape = "https://api.proxyscrape.com/?request=getproxies&proxytype={}&timeout=all&country=all"
        self.proxyscrape_v2 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol={}&timeout=all&country=all"
        self.proxy_list_download = "https://www.proxy-list.download/api/v1/get?type={}&anon=elite"
        self.session = rqs.Session()
        self.session.headers.update({("User-Agent", random.choice(user_agents))})


    def __proxyscrape(self,url):
        proxys = []
        response = self.session.get(url)
        p = response.text
        p = str(p).replace('\r','')
        p = p.split('\n')
        for proxy in p :
            if proxy not in proxy:
                proxys.append(proxy.replace('\n',''))
        return proxys
        
    def __proxyscrape_v3(self,type_):
        proxy_data = []
        res = rqs.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text')
        if res.ok :
            res = str(res.text).replace('\r','')
            res  = res.split('\n')
            for item in res:
                item = item.replace('//','').replace('\r','').replace('\n','')
                item = item.split(':')
                # print(item)
                if len(item) == 3:
                    proxy_dat = f"{item[1]}:{item[2]}"
                    if type_ == item[0]:
                        proxy_data.append(proxy_dat)
                    elif type_ == 'https' and item[0] == 'http':
                        proxy_data.append(proxy_dat)

                else:
                    pass
        
        return proxy_data

    def __us_proxy(self):
        proxys = []
        page = self.session.get("http://us-proxy.org")
        soup = BeautifulSoup(page.text, "html.parser")
        proxies = set()
        table = soup.find("table", attrs={"class": "table table-striped table-bordered"})
        for row in table.findAll("tr"):
            count = 0
            proxy = ""
            for cell in row.findAll("td"):
                if count == 1:
                    proxy += ":" + cell.text.replace("&nbsp;", "")
                    proxies.add(proxy)
                    break
                proxy += cell.text.replace("&nbsp;", "")
                count += 1
                
        for line in proxies:
            proxys.append(line)

        return proxys

    def __filter(self,proxys:list):
        new_proxy = []
        for proxy in proxys:
            if proxy not in new_proxy:
                new_proxy.append(proxy)

        return new_proxy


    def scrape(self,type_:str):
        type_ = type_.lower()
        if type_ in self.proxy_types:
            if type_ == 'all':
                proxy_types = ['http','https','socks4','socks5']
                p =[]
                for p_type in proxy_types:
                    proxyscrape = self.__proxyscrape(self.proxyscrape.format(p_type))
                    proxyscrape_v2 = self.__proxyscrape(self.proxyscrape_v2.format(p_type))
                    proxy_list_download = self.__proxyscrape(self.proxy_list_download.format(p_type))
                    proxyscrape_v3 = self.__proxyscrape_v3(p_type)
                    p.append(proxyscrape)
                    p.append(proxyscrape_v2)
                    p.append(proxy_list_download)
                    p.append(proxyscrape_v3)
                us_proxy = self.__us_proxy()
                proxy =[]
                for prox in p:
                    proxy+=prox
                proxy+= us_proxy
                filtered_proxy = self.__filter(proxy)
            else:
                proxyscrape = self.__proxyscrape(self.proxyscrape.format(type_))
                proxyscrape_v2 = self.__proxyscrape(self.proxyscrape_v2.format(type_))
                proxy_list_download = self.__proxyscrape(self.proxy_list_download.format(type_))
                proxyscrape_v3 = self.__proxyscrape_v3(type_)
                proxy = proxyscrape+proxyscrape_v2+proxyscrape_v3+proxy_list_download
                filtered_proxy = self.__filter(proxy)

            return filtered_proxy
        else:
            raise ProxyTypeError()
        
print(scrapeProxy().scrape('socks5'))