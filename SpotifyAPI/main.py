import aiohttp
import asyncio
import base64
import json

# Auth objects
BASE_URL = "https://accounts.spotify.com/api/token"

def read_config():
    try:
        file = open("config.json")
    except OSError:
        print("Could not open config file")
    
    with file:
        data = json.load(file)
        return data

async def authenticate():
    config = read_config()
    async with aiohttp.ClientSession() as session:
        async with session.post(BASE_URL,
                                data=config) as response:
            json_data = await response.text()
            print("Body:", json_data)

async def main():
    await authenticate()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())