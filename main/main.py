from asyncio import new_event_loop

from insta.bot import main as insta_bot


def main():
    loop = new_event_loop()
    loop.create_task(insta_bot())
    loop.run_forever()


if __name__ == '__main__':
    main()