#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def getCounts(session, instance, filter):
    if filter != None and len(filter) > 0:
        filter = " where "+filter
    else:
        filter=""
    lst = session.execute("select count(1) from "+instance.__tablename__+filter).fetchone()
    return lst[0]

def getEntities(session, model, filter):
    return session.query(model).filter(filter).all()

def newEntity(session, entity):
    session.add(entity)
    session.commit()

def delEntity(session, entity):
    session.delete(entity)
    session.commit()
    
def updateEntities(id, title, text):
    db.update('entries', where='id=$id', vars=locals(), title=title, context=text)
		