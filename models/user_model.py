from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
from db.database import db

class User(db.Model):
    __tablename__ = "users"
    id = Column('id', String(36), primary_key=True, default=uuid.uuid4)
    username = Column('username', String(40), nullable=False, unique=True)
    email = Column('email', String(40), unique=True)
    password = Column('password', String(99), nullable=False)



if __name__=='__main__':
    #Base = declarative_base()
    #engine = create_engine('mysql://root:12345@localhost/testdb', echo=True)
    #Base.metadata.create_all(engine)

    session = db.session

    new_user = User()
    new_user.username = 'Frank'
    new_user.password = 'TestDemo2223'

    session.add(new_user)
    res =session.commit()
    print(res)

    session.close()
