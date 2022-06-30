import asyncio
import aiohttp
import json

async def hoge():
    async with aiohttp.ClientSession() as sessiong:
        async with sessiong.get("https://ツイログ.総合サービス.com/%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E8%A9%B3%E7%B4%B0/readmore.php?type=statuses&user_id=1157577246791483392&date=201909&flag=-1") as responseg:
            oldtws = json.loads(await responseg.text())
            print(oldtws)

asyncio.run(hoge())