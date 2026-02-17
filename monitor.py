import aiohttp
import asyncio
import time

historial = {}

async def check_site(session, url):
    try:
        start = time.time()

        async with session.get(url, timeout=5) as response:
            latency = round(time.time() - start, 2)
            status = response.status

            if url not in historial:
                historial[url] = []

            historial[url].append(latency)

            return url, True, latency, status

    except:
        return url, False, 0, "ERROR"


async def monitor_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [check_site(session, site) for site in sites]
        return await asyncio.gather(*tasks)
