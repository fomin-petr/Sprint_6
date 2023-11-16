from pages.start_page import StartPage
import pytest


class TestImportantReplies:

    reply_order = [[0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                   [1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
                   [2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                   [3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                   [4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
                   [5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
                   [6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
                   [7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
                   ]

    @pytest.mark.parametrize('number, expected_reply', reply_order)
    def test_important_question_1(self, scooter_page, number, expected_reply):
        self.driver = scooter_page
        start_page = StartPage(self.driver)
        start_page.close_cookie_notify()
        start_page.click_important_question(number)
        important_reply = start_page.get_important_reply(number)
        assert important_reply == expected_reply
