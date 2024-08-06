#!/usr/bin/env python3
""""""

import asyncio


async def my_coroutine():
    print('Hello')
    await asyncio.sleep(5)
    print('World')


async def greet(name):
    print(f'Hello, {name}')
    await asyncio.sleep(1)
    print(f'Goodbye, {name}')


async def implement_greet():
    await asyncio.gather(greet('Alice'), greet('Bob'), greet('Charlie'))


async def main():
    print('Starting...')
    await my_coroutine()
    print('Finished....')


asyncio.run(implement_greet())
