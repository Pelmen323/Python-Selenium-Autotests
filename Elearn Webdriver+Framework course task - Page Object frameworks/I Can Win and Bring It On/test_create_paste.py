import pytest
from pages.create_paste_page import CreatePastePage
from pages.read_paste_page import ReadPastePage


class TestNewPaste:
    LINK = "https://paste.ee/"

    @pytest.mark.parametrize("paste_text", \
[('''git config --global user.name  "New Sheriff in Town"
git reset $(git commit-tree HEAD^{tree} -m "Legacy code")
git push origin master --force''')])
    @pytest.mark.parametrize("paste_expiration, paste_title, paste_syntax", [("1 hour", "how to gain dominance among developers", "Bash")])
    def test_guest_can_create_new_paste(self, browser, paste_text, paste_expiration, paste_title, paste_syntax):
        new_paste_page = CreatePastePage(browser=browser, url=TestNewPaste.LINK)
        new_paste_page.open()
        new_paste_page.add_text_to_paste(paste_text)
        new_paste_page.add_title_to_paste(paste_title)
        new_paste_page.select_syntax_highlighting(paste_syntax)
        new_paste_page.select_paste_expiration_time(paste_expiration)
        new_paste_page.submit_new_paste()
        read_paste_page = ReadPastePage(browser=browser, url=browser.current_url)
        read_paste_page.should_have_required_title(paste_title)
        read_paste_page.should_have_syntax_highlighted(paste_syntax)
        read_paste_page.should_have_body_text(paste_text)
