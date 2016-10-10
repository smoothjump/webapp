#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import web
from web.contrib.template import render_jinja

urls = (
    '/', 'Index'
    '/success','Success'
)
app = web.application(urls, globals())

render = render_jinja(
    'template', # 模板路径
    encoding='utf-8', #编码
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
        pass

if __name__ == "__main__":
    app.run()