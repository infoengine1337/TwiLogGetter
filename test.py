import asyncio

async def hoge():
    for i in range(10):
        print("hoge")

    return 10

async def parts():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(hoge()))

    return_lists = await asyncio.gather(*tasks)

    for i in return_lists:
        print(i)

if __name__ == '__main__':
    asyncio.run(parts())
    print("hg")