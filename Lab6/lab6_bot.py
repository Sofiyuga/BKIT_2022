from random import choice
import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text


msg_set1 = open('bad.txt', 'r', encoding='utf-8').read().splitlines()
msg_set2 = open('good.txt', 'r', encoding='utf-8').read().splitlines()
msg_set3 = open('you.txt', 'r', encoding='utf-8').read().splitlines()
bot = Bot('token')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Тут ТАКОЕ произошло...!", "Отличный день!", "Я молодец!)", "Тяжелый сегодня день, мне плохо("]
    keyboard.add(*buttons)
    await message.answer("Привет! Как прошел твой день?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Тяжелый сегодня день, мне плохо("))
async def first(message: types.Message):
    await message.answer("Возможно, тебе станет лучше, если ты поделишься, что произошло?")
    @dp.message_handler()
    async def message1(message: types.Message):
        await bot.send_message(message.chat.id, choice(msg_set1))
        

@dp.message_handler(Text(equals="Отличный день!"))
async def second(message: types.Message):
    await message.answer("Это прекрасно! Может, расскажешь подробнее?")
    @dp.message_handler()
    async def message2(message: types.Message):
        await bot.send_message(message.chat.id, choice(msg_set2))

@dp.message_handler(Text(equals="Я молодец!)"))
async def third(message: types.Message):
    await message.answer("Расскажи о своих достижениях, порадуемся вместе!")
    @dp.message_handler()  
    async def message3(message: types.Message):
        await bot.send_message(message.chat.id, choice(msg_set3))

@dp.message_handler(Text(equals="Тут ТАКОЕ произошло...!"))
async def fourth(message: types.Message):
    await message.answer("Сгораю от нетерпения! Рассказывай подробнее!!!")
    @dp.message_handler()
    async def message4(message: types.Message):
        photo = open('cat.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
