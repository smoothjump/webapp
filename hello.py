#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import web
from web.contrib.template import render_jinja
from models import User

urls = (
    "/", "Index",
    "/index", "Index",
    "/register", "Register",
    "/success", "Success",
)
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})
render = render_jinja(
    'template', # template default path
    encoding='utf-8', # encoding
)

class Index:
    form = web.form.Form(
        web.form.Textbox('login_name', web.form.notnull, size=30, description="Username"),
        web.form.Password('password', web.form.notnull, size=30, description="Password"),
        web.form.Button('Login'),
    )

    def GET(self):
    	form = self.form()
    	return render.index(form=form)

    def POST(self):
        form = self.form()
        if not form.validates():
            for r in form.inputs:
                r.set_value("")
            return render.index(form=form)
        user = User(login_name = form.d.login_name,password = form.d.password)
        if user.auth() == True:
            raise web.seeother('/success?user='+form.d.login_name)
        else:
            # Invalid auth info clear the original input
            for r in form.inputs:
                r.set_value("")
            return render.index(form=form)

class Success:
    def GET(self):
        vars = web.input()
        user = vars["user"]
        print user
        return render.success(user=user)

if __name__ == "__main__":
    app.run()