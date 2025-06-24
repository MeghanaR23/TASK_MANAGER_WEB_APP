from pydantic import BaseModel

class RegisterUser(BaseModel):
    username: str
    password: str
    
class UserLogin(BaseModel):
    username: str
    password: str