from asyncio import sleep

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils.executor import start_polling

from main.logs import Console
from resources_manager.config import get_config, Keys
from resources_manager.database import change_status, add_user, get_status
from resources_manager.messages import get_messages, MessageKeys

bot = Bot(get_config(Keys.TelegramBotToken))
db = Dispatcher(bot)
console = Console('Telegram bot')


async def main():
    try:
        await sleep(5)
        console.start()
        start_polling(dispatcher=db)
    except Exception as e:
        print(e)


@db.message_handler(commands=['start', 'help'])
async def start(message: Message):
    add_user(message.chat.id)
    await bot.send_message(get_messages(MessageKeys.start), message.chat.id)


@db.message_handler(commands=['on_receive', 'off_receive'])
async def turn_status_receive(message: Message):
    old_status = get_status(message.chat.id)

    if 'on' in message.text:
        new_status = True
    else:
        new_status = False

    change_status(message.chat.id, new_status)
    await bot.send_message(get_messages(f'turn_status_receive_{old_status}_{new_status}'), message.chat.id)


async def sender():
    while True:
        await sleep(10)
