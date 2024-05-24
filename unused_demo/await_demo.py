import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['https://www.example.com', 'https://www.example.org', 'https://www.example.net']
    tasks = [fetch(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    for url, response in zip(urls, responses):
        print(f'{url}: {response[:100]}')

if __name__ == '__main__':
    asyncio.run(main())
