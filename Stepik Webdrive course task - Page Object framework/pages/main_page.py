from .base_page import BasePage


class MainPage(BasePage):
    '''
    Class the main website page
    '''
    
    def __init__(self, *args, **kwargs) -> object:
        super(MainPage, self).__init__(*args, **kwargs)
