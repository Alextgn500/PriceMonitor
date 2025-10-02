from app.core.config import settings
from aiogram import Bot
import asyncio

async def test_with_settings():
    print(f"Token from settings: '{settings.bot_token}'")
    print(f"Token length: {len(settings.bot_token) if settings.bot_token else 0}")
    
    try:
        bot = Bot(token=settings.bot_token)
        me = await bot.get_me()
        print(f'Бот через settings: {me.first_name}')
        await bot.session.close()
    except Exception as e:
        print(f'Ошибка с settings: {e}')
        print(f'Тип ошибки: {type(e)}')

if __name__ == '__main__':
    asyncio.run(test_with_settings())
