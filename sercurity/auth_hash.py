from decouple import config
from passlib.context import CryptContext



JWT_SECRET = config("secret")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password, salt= JWT_SECRET )


