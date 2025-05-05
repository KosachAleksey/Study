import asyncio
import time

start = time.time()

async def fetch_data():
    print(" Starts downloading data")
    await asyncio.sleep(5)
    print("The data is uploaded!")
    return "result"

async def main():
    await asyncio.gather(fetch_data() for i in range (1000))


asyncio.run(fetch_data())
end = time.time() - start
print(end)