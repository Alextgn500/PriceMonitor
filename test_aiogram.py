import asyncio
from aiogram import Bot

async def test_bot():
    token = ''
    try:
        bot = Bot(token=token)
        me = await bot.get_me()
        print(f'Бот создан успешно: {me.first_name} (@{me.username})')
        await bot.session.close()
    except Exception as e:
        print(f'Ошибка создания бота: {e}')

if __name__ == '__main__':
    asyncio.run(test_bot())
