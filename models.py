from sqlalchemy import Column, Integer, String,Float,Foreignkey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base


#user model

class User(Base):
    
    _tablename_ = "users"
    id = Column (String, Primary_key = True)
    username = Column(String, unique = True, nullable = False)
    pin_hush = Column(String, nullable = False)
    
    
    accounts = relationship ("Account", back_populates= "owner")
    
