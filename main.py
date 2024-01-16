import os

from dotenv import load_dotenv

from simple_telegram_bot import Bot


def main():
    load_dotenv()

    bot_token = os.getenv('BOT_TOKEN', None)
    if not bot_token:
        raise ValueError('BOT_TOKEN is not define')

    bot = Bot(bot_token)
    bot.run()


if __name__ == '__main__':
    main()
