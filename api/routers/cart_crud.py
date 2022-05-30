from fastapi import  APIRouter, Depends
from services import  carts_services
from sqlalchemy.orm import Session
from core.engine import create_session
from schemas import   Cart,  CartCreate , CartUpdate
from sercurity import JWTBearer,decodeJWT   



router = APIRouter()



@router.get("/", tags=["cart"], response_model=  Cart)
async def get_cart( session: Session = Depends(create_session),
                        credentials: str = Depends(
                        JWTBearer(["admin","manager","staff","customer"]))):
    return  carts_services.show_carts(session,credentials)



@router.post("/{id}", tags=["cart"], response_model= Cart)
async def create_cart(cart_schemas:  CartCreate , session: Session = Depends(create_session),
                        credentials: str = Depends(
                        JWTBearer(["customer"]))):
     return  carts_services.buy_book(session, cart_schemas,credentials )
 

# @router.put("/", tags=["cart"], response_model= Cart)
# async def update_a_cart( id: int, cart_schemas:  CartUpdate, session: Session = Depends(create_session),
#                         credentials: str = Depends(
#                         JWTBearer(["customer"]))):
#      return  carts_services.modify_cart(session,id, cart_schemas,credentials)



@router.delete("/{id}", tags=["cart"])
async def delete_cart( id: int ,session: Session = Depends(create_session),
                        credentials: str = Depends(
                        JWTBearer(["customer","admin"]))):
     return carts_services.remove_cart(session,id,credentials)
        
      



 
 