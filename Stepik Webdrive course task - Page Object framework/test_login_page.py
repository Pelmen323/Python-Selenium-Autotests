from .pages.login_page import LoginPage


def test_verify_login_page_is_valid(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser=browser, url=link)
    page.open()
    page.should_be_login_page()
