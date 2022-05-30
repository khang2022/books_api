from fastapi import HTTPException
from dbmodels import Carts, BookCartTable, Books
from .services_base import BaseService,Session
from .books_services import books_services
from schemas import CartCreate
from sercurity import decodeJWT
from fastapi.encoders import jsonable_encoder  



class CartsService(BaseService[Carts]):
    
    
     def show_carts(self, session: Session ,credentials : str):
            payload = decodeJWT(credentials) 
            if payload["role"] == "customer":
                return session.query(Carts).filter(Carts.customer_id == payload["id"]).all() # show cart by staff 
            else:
                a = session.query(Carts).all()
                print(jsonable_encoder(a))
                #  return session.query(Carts).all() # show cart by internal 
             
               
     def buy_book( self, session: Session ,cart_schemas: CartCreate, credentials :str):
            payload = decodeJWT(credentials) 
            new_cart = Carts(
                customer_id = payload["id"], 
                purchase_date = cart_schemas.purchase_date,
                paymented     = cart_schemas.paymented  
            ) 
            # check book id có tồn tại hay không?
            books_available = session.query(Books).filter(Books.id.in_(cart_schemas.books_list)).all()
            if not books_available: # nếu như thiếu 1 id sẽ ngay lập tức báo lỗi
                raise HTTPException(status_code= 404,  detail="Books are missing !")
            new_cart.books_list = books_available
            # print(jsonable_encoder(new_cart))
            return self.save( session, new_cart)
        
        
    #  def  modify_cart(self, session: Session,id : int, cart_schemas: CartCreate,credentials :str):
    #         payload = decodeJWT(credentials)    
          
            
            
     def remove_cart(self, session: Session,id : int, credentials: str):
            payload = decodeJWT(credentials) 
            if payload["role"] == "customer":
                available = session.query(Carts).filter_by(Carts.id == id,Carts.customer_id == payload["id"]).first()
                if not available:
                    raise HTTPException(
                        status_code=404,  detail="This cart is not exist !")
                self.delete_one(session, id)
            else:
                available = session.query(Carts).filter(Carts.id == id).first()
                if not available:
                    raise HTTPException(
                        status_code=404,  detail="This cart is not exist !")
                self.delete_one(session, id)           
            
           
carts_services = CartsService(Carts) 

