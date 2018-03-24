# coding: utf-8

from app import app

from app.dept import dept
from app.user import user

app.register_blueprint(user, url_prefix='/user')
app.register_buleprint(dept, url_prefix='/dept')

if __name__ == '__main__':
    app.run()

