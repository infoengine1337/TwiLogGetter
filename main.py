import asyncio
import aiohttp
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
import pickle

def month_span(begindate_obj, enddate_obj):
    yield begindate_obj
    while(begindate_obj.year != enddate_obj.year or begindate_obj.month != enddate_obj.month):
        begindate_obj = begindate_obj + relativedelta(months=-1)
        yield begindate_obj


def name2id(tmp_name):
    r = requests.get("https://idtwi.com/search/" + tmp_name)
    sp = BeautifulSoup(r.text,"html.parser")
    id, createdate = sp.find_all('b')[1].text, sp.find_all('dd')[2].text
    return id, createdate

async def fetch_log_per_month(userid, yearmonth):

    URL = "https://xn--eckyazdvi.xn--vcki1fxh883oon2c.com/%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E8%A9%B3%E7%B4%B0/readmore.php?type=statuses"
    log_result = []

    yearmonth_str = yearmonth.strftime('%Y%m')
    print(yearmonth_str,end=' ')

    async with aiohttp.ClientSession() as session:
        lasttwtime = "-1"
        while True:
            async with session.get(URL, params={"user_id":userid,"date":yearmonth_str,"flag":lasttwtime} ) as response:
                oldtws = json.loads(await response.text())
                if not oldtws["data"]:
                    print("There is No Tweet in {}...".format(yearmonth_str))
                    break
                else:
                    for oldtw in oldtws["data"]:

                        log_result.append({"month": yearmonth_str, "text": oldtw["text"].replace("\n",""), "created_at": oldtw["created_at"]})
                        
                        lasttwtime = oldtw["id"]

                if len(oldtws["data"]) < 15:
                    print("Tweet in {} is ended.".format(yearmonth_str))
                    break

        return log_result
                


async def main():
    
    id = 0
    returnval_lists = []
    name = input("Please Enter Twitter screenname:")

    id, createdate = name2id(name)
    print("User {} -> {}".format(name, id))

    createdate_obj, nowdate_obj = datetime.strptime(createdate,'%Y/%m/%d'), datetime.now()

    tasks_list = []
    for aimdate in month_span(nowdate_obj,createdate_obj):

        tasks_list.append(asyncio.create_task(fetch_log_per_month(id, aimdate)))
        
    returnval_lists = await asyncio.gather(*tasks_list)

    print(returnval_lists)

    with open("{}.pkl".format(name), 'wb') as file:
        pickle.dump(returnval_lists, file)

    print("Succeed.")
        

if __name__ == '__main__':
    asyncio.run(main())