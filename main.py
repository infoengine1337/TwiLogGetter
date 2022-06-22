import asyncio
import aiohttp
import json
import requests
from bs4 import BeautifulSoup

def name2id(tmp_name):
    r = requests.get("https://idtwi.com/search/" + name)
    sp = BeautifulSoup(r.text,"html.parser")
    
    sp = BeautifulSoup(r.text,"html.parser")
    id, createdate = sp.find_all('b')[1].text, sooopu.find_all('dd')[2].text
    createdate_obj, lastdate_obj =  datetime.strptime(createdate,'%Y/%m/%d'), datetime.now()



async def fetch_log_per_month( month):

    async with aiohttp.ClientSession() as session:
        for i in range():
            async with session.get(dest_url) as response:
#                print("Status:", response.status)



def main():
    
    id = 0
    name = input("Please Enter Twitter screenname:")


    #with open("{}.csv".format(name), 'w', encoding='utf-8') as f:

    id = name2id(name)


    asyncio.run(donate_ukraine())
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

if __name__ == '__main__':
    main()