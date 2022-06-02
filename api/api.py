from fastapi import APIRouter
from .routers import book, cart, customer, login, role, staff

api_router = APIRouter()

api_router.include_router(
    login.router, prefix="/login", tags=["login"])
api_router.include_router(staff.router, prefix="/staff", tags=["staff"])
api_router.include_router(customer.router,
                          prefix="/customer", tags=["customer"])
api_router.include_router(cart.router, prefix="/cart", tags=["cart"])
api_router.include_router(book.router, prefix="/book", tags=["book"])
