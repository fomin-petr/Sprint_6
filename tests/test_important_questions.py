from pages.start_page import StartPage
import pytest
from tests.data import DataForTests


class TestImportantReplies:

    @pytest.mark.parametrize('number, expected_reply', DataForTests.reply_order)
    def test_important_question_1(self, scooter_page, number, expected_reply):
        self.driver = scooter_page
        start_page = StartPage(self.driver)
        start_page.close_cookie_notify()
        start_page.click_important_question(number)
        important_reply = start_page.get_important_reply(number)
        assert important_reply == expected_reply
