from .base_page import BasePage
from .locators import ReadPastePageLocators


class ReadPastePage(BasePage):
    def should_have_required_title(self, expected_title: str):
        title_contents = self.browser.find_element(*ReadPastePageLocators.PASTE_INFO_CONTAINER).get_attribute('data-name')
        assert title_contents == expected_title, f"Title of the paste doesnt't match the passed title. Expected '{expected_title}', but found '{title_contents}'"

    def should_have_body_text(self, expected_paste_body: str):
        self.browser.find_element(*ReadPastePageLocators.PASTE_SWITCH_TO_RAW_FORMAT).click()
        actual_paste_body = self.browser.find_element(*ReadPastePageLocators.PASTE_TEXT_AREA).get_attribute("value")
        assert actual_paste_body == expected_paste_body, f"Title of the paste doesnt't match the passed title. Expected '{expected_paste_body}', but found '{actual_paste_body}'"

    def should_have_syntax_highlighted(self, expected_syntax: str):
        syntax_text = self.browser.find_element(*ReadPastePageLocators.PASTE_INFO_CONTAINER).get_attribute('data-syntax')
        assert syntax_text == expected_syntax.lower(), f"Syntax of the paste doesnt't match the passed syntax. Expected '{expected_syntax}', but found '{syntax_text}'"
