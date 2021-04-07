from asyncio import new_event_loop

from insta.bot import main as insta_bot
from teleg.bot import main as telegram_bot


def main():
    loop = new_event_loop()
    loop.create_task(insta_bot())
    loop.create_task(telegram_bot())
    loop.run_forever()


if __name__ == '__main__':
    main()
