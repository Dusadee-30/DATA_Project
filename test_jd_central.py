import re, json, requests
from config import *
import html
import urllib
import pandas as pd


if __name__ == "__main__":
    keyword_search = input("search : ")
    print('-' * 100)

    keyword_jd_central = urllib.parse.quote(keyword_search)
    
    HEADER_JD_CENTRAL["Referer"] = HEADER_JD_CENTRAL["Referer"].format(jd_central = URL_WEB_JD_CENTRAL, keyword = keyword_jd_central)
    URL_SEARCH_JD_CENTRAL = URL_SEARCH_JD_CENTRAL.format(keyword =keyword_jd_central)

    res = requests.get(URL_SEARCH_JD_CENTRAL, headers = HEADER_JD_CENTRAL).json()

    print(res)
    """""
    lstshopee = []
    for item in res["items"]:
        image_link = requests.get(URL_IMAGE_SHOPEE+str(item['item_basic']['image']))
        #img = Image.open(BytesIO(image_link.content))
        #img.show()
        print(item['item_basic']['name'])
        if (int(item['item_basic']['price_min']) != int(item['item_basic']['price_max'])):
            print("price min : ",int(item['item_basic']['price_min'])/100000,"บาท |  price max : ",int(item['item_basic']['price_max'])/100000 ,"บาท")
        else:
            print("price : ",int(item['item_basic']['price'])/100000,"บาท")
        taillink = item['item_basic']['name']
        newtaillink = taillink.replace(" ","-")
        link = URL_LINK_ITEM_SHOPEE+newtaillink
        link = link +'-i.'+ str(item['item_basic']['shopid'])+'.'+str(item['item_basic']['itemid'])
        print(link)
        lstshopee.append(item['item_basic']['name'])
        print("-" * 100)
  
"""