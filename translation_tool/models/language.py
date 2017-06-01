# this python file uses the following encoding utf-8

from translation_tool import db


class Language(db.Model):
    code = db.Column(db.String(8), unique=True, primary_key=True)

    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return '<Language %r>' % (self.code)
