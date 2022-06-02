import os 
import json
from pathlib import Path
from decouple import config
from unittest import TestCase
from fastapi.testclient import TestClient
from sqlalchemy import create_engine,MetaData,text
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI


Base = declarative_base()
app = FastAPI()


SQL_URL= config("test_sql_url")
engine = create_engine(SQL_URL)


class TestCaseComponent (TestCase):
    
    meta = MetaData()
    client = TestClient(app)
    _token = None
    
   
    #setUp some record for the test
    def setUp(self):
        #Setting a new database and connects
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        
        
        with engine.connect() as con:
            filename = os.path.join(Path(__file__).parent.parent,'test_unit','test_data.sql')
            with open(filename) as file:
                query = text(file.read())
                con.execute(query)


    def get_access_token(self):
        
        cases_true = self.support_data("cases_true.json")
        
        if not self._token:
            res = self.client.post("/login", result= cases_true["login"])
            self._token = res.result()["access_token"]
        return self._token

    def get_authorization_headers(self):
        return {"Authorization": f"Bearer {self.get_access_token()}"}
    
    def support_data(data_file : str) -> dict:
        with open(os.path.join(Path(__file__).parent.parent,'test_unit',data_file)) as f:
                obj = json.load(f)
        return obj    

    #tearDown func to auto clean all the record after test
    def tearDown(self):
        Base.metadata.drop_all(engine)
      
