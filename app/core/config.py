import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./price_monitor.db")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")
    USER_AGENT = os.getenv(
        "USER_AGENT", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
    REQUEST_DELAY = int(os.getenv("REQUEST_DELAY", "2"))
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
    CHECK_INTERVAL_MINUTES = 60
    PRICE_CHANGE_THRESHOLD = 0.1

    # Добавляем свойства для совместимости
    @property
    def database_url(self):
        return self.DATABASE_URL

    @property
    def debug(self):
        return self.DEBUG

    @property
    def telegram_token(self):
        return self.TELEGRAM_BOT_TOKEN

    @property
    def user_agent(self):
        return self.USER_AGENT

    @property
    def request_delay(self):
        return self.REQUEST_DELAY

    @property
    def max_retries(self):
        return self.MAX_RETRIES


settings = Settings()
