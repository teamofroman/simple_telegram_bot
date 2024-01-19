import json
from http import HTTPStatus

import aiohttp
import asyncio

from constants import BASE_URL, GET_UPDATES_DELAY
from .structures import User
from .exeptions import (
    BotGetDataErrorException,
    BotResponseStructureErrorException
)


class Bot:
    def __init__(self, bot_token: str):
        self.bot_token: str = bot_token
        self.bot_info: User | None = None

    async def __send_request(
            self,
            method: str,
            data: str | None = None,
    ):
        url = BASE_URL.format(token=self.bot_token, method=method)
        if not data:
            data = {}

        async with aiohttp.ClientSession() as session:
            try:
                response = await session.post(url, data=json.dumps(data))
            except Exception as e:
                response = None
                print(e)

        if not response:
            return None

        if response.status != HTTPStatus.OK:
            return None

        return await response.json()

    async def __get_bot_info(self) -> User:
        user_json = await self.__send_request('getMe')
        if not user_json.get('ok', False):
            raise BotGetDataErrorException(
                'ERROR: Get bot info\n'
                f'Error code {user_json["error_code"]}\n'
                f'Description {user_json["description"]}'
            )

        result = user_json.get('result', None)
        if not result:
            raise BotResponseStructureErrorException(
                'ERROR: Parameter `result` is missing'
            )

        if 'id' not in result:
            raise BotResponseStructureErrorException(
                'ERROR: Parameter `id` is missing'
            )

        if 'is_bot' not in result:
            raise BotResponseStructureErrorException(
                'ERROR: Parameter `is_bot` is missing'
            )

        if 'first_name' not in result:
            raise BotResponseStructureErrorException(
                'ERROR: Parameter `first_name` is missing'
            )

        return User(**result)

    async def __async_run(self):
        self.bot_info = await self.__get_bot_info()
        while True:
            try:
                update_info = await self.__send_request('getUpdates')
                if update_info['ok']:
                    result = update_info['result']
                    if result:
                        ...
                else:
                    message = (f'BOT API ERROR: Code '
                               f'{update_info["error_code"]}'
                               f'Description {update_info["description"]}'
                               )
                    print(message)
                # print(update_info)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f'ERROR: {e}')
            finally:
                await asyncio.sleep(GET_UPDATES_DELAY)

    def run(self):
        try:
            asyncio.run(self.__async_run())
        except KeyboardInterrupt:
            pass