from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.services.repository import Repo
from tgbot.states.user import UserMain

from ntobot.src.tgbot.services.repository import CSVRepo


async def user_start(m: Message, state: FSMContext, repo: Repo = CSVRepo):
    await m.reply("Hello, user!")
    await state.set_state(UserMain.SOME_STATE)


async def user_data(m: Message, state: FSMContext, repo: Repo = CSVRepo):
    await m.reply("Data:")
    await state.set_state(UserMain.SOME_STATE)
    data = await repo.get_age_data()
    await m.reply(data)

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_data, commands=["get_age_data"], state="*")
