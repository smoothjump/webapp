#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine, Integer, NVARCHAR
from dbutils import getCounts, newEntity
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

# Database initialization:
engine = create_engine('mysql+mysqldb://root:123@localhost:3306/test?charset=utf8', echo = True, pool_size = 10)
# create DBSession:
DBSession = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    # Table Name:
    __tablename__ = 'users'
    # Table defination:
    id = Column(Integer, primary_key = True)
    login_name = Column(String(20))
    name = Column(NVARCHAR(20))
    password = Column(String(20))
    session = DBSession()

    def auth(self):
    	cnt = getCounts(self.session, self, "login_name=\'"+self.login_name+"\' and password=\'"+self.password+"\'")
    	if cnt > 0:
    		return True
    	else:
    		return False

    def add(self):
    	newEntity(self.session, self)

if __name__=='__main__':
	new_user = User(login_name='arlen', name='赵笋',password='123')
	session = new_user.session
	users = session.query(User).filter(text("login_name='arlen'")).all()
	for usr in users:
		print usr.id
		print usr.name