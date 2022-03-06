import asyncio
from typing import Iterable, NamedTuple

import aiohttp


class Result(NamedTuple):
    status_code: int
    content: int


async def fetch(url, session):
    async with session.get(url) as response:
        if response.status == 200:
            content = await response.text()
        else:
            content = 0
        return Result(status_code=response.status, content=int(content))


async def get_results_from_urls(address: str, port: int, slugs: list) -> Iterable[Result]:
    """Get results from http responses.

     Get responses by making requests to urls.
     Construct url like this: {address}:{port}/{slug}, where address and port are constant, but slug changes.
     Result.status_code is status code of response.
     Result.content is content of response if status_code is 200, otherwise it is 0.
     Results must be ordered according to the order of slugs in list and their respective responses.
     Requests must be sent in a asynchronous way. (Can not be sequential and blocking.)
     """
    tasks = []
    async with aiohttp.ClientSession() as session:
        for slug in slugs:
            task = asyncio.ensure_future(fetch(f"{address}:{port}/{slug}", session))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses

