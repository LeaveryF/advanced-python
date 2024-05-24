import asyncio

async def hello_world():
    print("Hello World!")
    await asyncio.sleep(1)

async def main():
    task = asyncio.create_task(hello_world())
    await task

asyncio.run(main())
