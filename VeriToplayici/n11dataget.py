#-*- coding: latin-1 -*-

import requests
from htmlAdaptor import HtmlGet


header = {}

header['Host'] = "urun.n11.com"
header['Accept'] = 'text/html, */*; q=0.01'
header['Accept-Encoding'] = 'gzip, deflate, br'
header['Accept-Language'] = 'en-US,en;q=0.5'
header['Connection']= 'keep-alive'
header['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
#header['Cookie'] = 'citrix_ns_id=/t8/OehuyKrm3LINI…a-6930-4c91-8102-df1e85628d56'
#header['Host'] = 'urun.n11.com'
#header['Referer'] = 'https://urun.n11.com/sac-kurut…ac-kurutma-makinesi-P256180546'
header['requestType'] = 'AJAX'
header['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/60.0'
header['X-Requested-With'] = 'XMLHttpRequest'



#page = input("page number: ")
fl = open("links","r")
links = fl.read().split()
fl.close()
for link in links:
    productId = link.split("P")[-1]
    fl = open(productId,"a+")
    page = "1"
    i= 2
    while(1):
        url = "https://urun.n11.com/component/render/productReviews?page="+page+"&productId="+productId
        header['Referer'] = link
        response = requests.get(url,headers = header)
        ht = HtmlGet()
        data = ht.getData(response.text)
        if(len(data) == []):
            break
        for i in data:
            fl.write(i + "\n")
        page = str(i)
        i += 1
fl.close()
