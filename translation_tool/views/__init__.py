# this python file uses the following encoding utf-8

from .languages import LanguageView
from translation_tool import app

language_view = LanguageView.as_view('languages')
app.add_url_rule('/languages/', defaults={'language_code': None},
                 view_func=language_view, methods=['GET'])
app.add_url_rule('/languages/', view_func=language_view, methods=['POST'])
app.add_url_rule('/languages/<string:language_code>', view_func=language_view,
                 methods=['GET', 'PUT', 'DELETE'])
