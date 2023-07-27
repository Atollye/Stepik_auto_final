from pages.base_page import BasePage


LINK_TO_PAGE = "http://selenium1py.pythonanywhere.com"


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
