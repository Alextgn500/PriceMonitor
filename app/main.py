from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import router

app = FastAPI(
    title="Price Monitor API",
    description="API для мониторинга цен на товары",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене указать конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роуты
app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Price Monitor API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
