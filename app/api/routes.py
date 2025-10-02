from fastapi import APIRouter

router = APIRouter()

@router.get("/products")
async def get_products():
    return {"message": "Список товаров"}

@router.post("/products/track")
async def track_product():
    return {"message": "Товар добавлен в отслеживание"}

@router.get("/prices/{product_id}")
async def get_price_history(product_id: int):
    return {"message": f"История цен для товара {product_id}"}
