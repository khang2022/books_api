from condition_setup import TestCaseComponent
from passlib.context import CryptContext  
from decouple import config   

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

JWT_SECRET = config("secret")



class TestLogin(TestCaseComponent):
    
    
    def get_password_hash(self,password):
        return pwd_context.hash(password, salt= JWT_SECRET )
   
    # Test login with success data - success user_name and pass
    def test_login(self):
        cases_true = self.support_data("cases_true.json")
       
        response = self.client.post("/login", json=cases_true["login"])
        assert response.status_code == 200
        assert response.json()["access_token"]

    # Test login with fail data
    def test_login_fail(self):
        cases_false = self.support_data("cases_false.json")
       
        response = self.client.post("/login", json=cases_false["login"])
        assert response.status_code == 400
        assert response.json()["detail"] == "Invalid login detail!"
