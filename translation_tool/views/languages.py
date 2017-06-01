# this python file uses the following encoding utf-8

from flask.views import MethodView
from translation_tool.models import Language


class LanguageView(MethodView):
    def get(self, language_code):
        if language_code is None:
            # return list of languages
            return ''
        else:
            # return single language
            pass

    def post(self):
        # create a new language
        pass
