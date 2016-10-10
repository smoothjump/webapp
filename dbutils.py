#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String, create_engine, Integer, NVARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
# 初始化数据库连接:
engine = create_engine('mysql+mysqldb://admin:123@localhost:3306/test?charset=utf8', echo = True, pool_size = 10)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'users'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    login_name = Column(String(20))
    name = Column(NVARCHAR(20))
    password = Column(String(20))

# class BaseHandler(object):
# 	"""Base Handler for ORM"""
# 	def __init__(self, arg):
# 		self.session = DBSession()
# 	def addItem(obj):
# 		self.session.add(obj)
# 		self.session.commit()
if __name__=='__main__':
	session = DBSession()
	new_user = User(login_name='arlen', name='李智',password='123')
	session.add(new_user)
	session.commit()
		