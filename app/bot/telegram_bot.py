import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, BotCommand
from aiogram.filters.command import Command
from app.services.price_monitor import PriceMonitorService

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = ""

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

price_service = PriceMonitorService()

@dp.message(Command("start"))
async def start_handler(message: Message):
    text = """ Добро пожаловать в Price Monitor Bot!

 Отправьте ссылку на товар для мониторинга цены.

 Поддерживаемые магазины:
 Wildberries
 DNS Shop

 Команды:
/start - начать
/help - справка"""
    
    await message.reply(text)

@dp.message(Command("help"))
async def help_handler(message: Message):
    text = """ Справка:

 Просто отправьте ссылку на товар
 Бот найдет цену и добавит в мониторинг

Примеры:
https://www.wildberries.ru/catalog/123456/detail.aspx
https://www.dns-shop.ru/product/товар"""
    
    await message.reply(text)

@dp.message(F.text.regexp(r'https?://.*'))
async def price_handler(message: Message):
    try:
        url = message.text.strip()
        print(f" Новый запрос: {url}")
        
        processing_msg = await message.reply(" Обрабатываем...")
        
        result = await price_service.check_price(url)
        print(f" Результат: {result}")
        
        await processing_msg.delete()
        
        if result['success']:
            data = result['data']
            
            text = f""" Товар найден!

 {data.get('name', 'Товар')}
 Цена: {data.get('price', '0')} 
 Магазин: {data.get('store', 'Неизвестно')}
 {' В наличии' if data.get('available', True) else ' Нет в наличии'}

Мониторинг добавлен!"""
            
            await message.reply(text)
        else:
            await message.reply(f" Ошибка: {result['error']}")
            
    except Exception as e:
        print(f" Ошибка: {e}")
        await message.reply(" Произошла ошибка")

@dp.message()
async def unknown_handler(message: Message):
    await message.reply(" Отправьте ссылку на товар или используйте /help")

async def main():
    print(" Запуск бота...")
    
    try:
        me = await bot.get_me()
        print(f" Бот: @{me.username}")
        
        commands = [
            BotCommand(command="start", description=" Начать"),
            BotCommand(command="help", description=" Справка"),
        ]
        await bot.set_my_commands(commands)
        
        print(" Бот готов!")
        await dp.start_polling(bot)
        
    except Exception as e:
        print(f" Ошибка: {e}")

if __name__ == '__main__':
    asyncio.run(main())
